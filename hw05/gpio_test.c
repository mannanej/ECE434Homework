/**
 * @file   gpio_test.c
 * @author Derek Molloy
 * @date   8 November 2015
 * @brief  A kernel module for controlling a GPIO LED/button pair. The
 * device mounts an LED and pushbutton via sysfs /sys/class/gpio/gpio60
 * and gpio46 respectively. */

#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/gpio.h>                 // for the GPIO functions
#include <linux/interrupt.h>            // for the IRQ code

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Derek Molloy");
MODULE_DESCRIPTION("A Button/LED test driver for the Beagle");
MODULE_VERSION("0.1");

static unsigned int gpioLED1 = 60;       // P9_12/P2.8 (GPIO60)
static unsigned int gpioLED2 = 50;       // P9_14 (GPIO50)
static unsigned int gpioButton1 = 46;    // P8_16/P2.22 (GPIO46)
static unsigned int gpioButton2 = 65;    // P8_18 (GPIO65)
static unsigned int irqNumber1;          // share IRQ num within file
static unsigned int irqNumber2;          // share IRQ num within file
static unsigned int numberPresses = 0;  // store number of presses
static bool	    led1On = 0;          // used to invert state of LED
static bool	    led2On = 0;          // used to invert state of LED

// prototype for the custom IRQ handler function, function below
static irq_handler_t  ebb_gpio_irq_handler1(unsigned int irq, void
                                    *dev_id, struct pt_regs *regs);
static irq_handler_t  ebb_gpio_irq_handler2(unsigned int irq, void
                                    *dev_id, struct pt_regs *regs);

/** @brief The LKM initialization function */
static int __init ebb_gpio_init(void){
   int result1 = 0;
   int result2 = 0;
   printk(KERN_INFO "GPIO_TEST: Initializing the GPIO_TEST LKM\n");
   if (!gpio_is_valid(gpioLED1)){
      printk(KERN_INFO "GPIO_TEST: invalid LED GPIO1\n");
      return -ENODEV;
   }
   if (!gpio_is_valid(gpioLED2)){
      printk(KERN_INFO "GPIO_TEST: invalid LED GPIO2\n");
      return -ENODEV;
   }
   led1On = true;
   led2On = true;
   gpio_request(gpioLED1, "sysfs");          // request LED GPIO1
   gpio_request(gpioLED2, "sysfs");          // request LED GPIO2
   gpio_direction_output(gpioLED1, led1On);   // set in output mode and on
   gpio_direction_output(gpioLED2, led2On);   // set in output mode and on
   gpio_export(gpioLED1, false);             // appears in /sys/class/gpio
   gpio_export(gpioLED2, false);             // appears in /sys/class/gpio
			               // false prevents direction change
   gpio_request(gpioButton1, "sysfs");       // set up gpioButton1
   gpio_request(gpioButton2, "sysfs");       // set up gpioButton2
   gpio_direction_input(gpioButton1);        // set up as input
   gpio_direction_input(gpioButton2);        // set up as input
// gpio_set_debounce(gpioButton1, 200);      // debounce delay of 200ms
// gpio_set_debounce(gpioButton2, 200);      // debounce delay of 200ms
   gpio_export(gpioButton1, false);          // appears in /sys/class/gpio
   gpio_export(gpioButton2, false);          // appears in /sys/class/gpio

   printk(KERN_INFO "GPIO1_TEST: button value is currently: %d\n",
          gpio_get_value(gpioButton1));
   irqNumber1 = gpio_to_irq(gpioButton1);     // map GPIO to IRQ number
   printk(KERN_INFO "GPIO2_TEST: button value is currently: %d\n",
          gpio_get_value(gpioButton2));
   irqNumber2 = gpio_to_irq(gpioButton2);     // map GPIO to IRQ number
   printk(KERN_INFO "GPIO_TEST: button mapped to IRQ: %d\n", irqNumber1);
   printk(KERN_INFO "GPIO_TEST: button mapped to IRQ: %d\n", irqNumber2);

   // This next call requests an interrupt line
   result1 = request_irq(irqNumber1,         // interrupt number requested
            (irq_handler_t) ebb_gpio_irq_handler1, // handler function
            IRQF_TRIGGER_RISING | IRQF_TRIGGER_FALLING,  // on rising edge (press, not release)
            "ebb_gpio_handler",  // used in /proc/interrupts
            NULL);                // *dev_id for shared interrupt lines
   result2 = request_irq(irqNumber2,         // interrupt number requested
            (irq_handler_t) ebb_gpio_irq_handler2, // handler function
            IRQF_TRIGGER_RISING | IRQF_TRIGGER_FALLING,  // on rising edge (press, not release)
            "ebb_gpio_handler",  // used in /proc/interrupts
            NULL);                // *dev_id for shared interrupt lines
   printk(KERN_INFO "GPIO_TEST: IRQ request result is: %d\n", result1);
   printk(KERN_INFO "GPIO_TEST: IRQ request result is: %d\n", result2);
   return result1;
}

/** @brief The LKM cleanup function  */
static void __exit ebb_gpio_exit(void){
   printk(KERN_INFO "GPIO_TEST: button value is currently: %d\n",
         gpio_get_value(gpioButton1));
   printk(KERN_INFO "GPIO_TEST: button value is currently: %d\n",
         gpio_get_value(gpioButton2));
   printk(KERN_INFO "GPIO_TEST: pressed %d times\n", numberPresses);
   gpio_set_value(gpioLED1, 0);    // turn the LED1 off
   gpio_set_value(gpioLED2, 0);    // turn the LED2 off
   gpio_unexport(gpioLED1);        // unexport the LED GPIO1
   gpio_unexport(gpioLED2);        // unexport the LED GPIO2
   free_irq(irqNumber1, NULL);     // free the IRQ number, no *dev_id
   free_irq(irqNumber2, NULL);     // free the IRQ number, no *dev_id
   gpio_unexport(gpioButton1);     // unexport the Button GPIO1
   gpio_unexport(gpioButton2);     // unexport the Button GPIO2
   gpio_free(gpioLED1);            // free the LED GPIO1
   gpio_free(gpioLED2);            // free the LED GPIO2
   gpio_free(gpioButton1);         // free the Button GPIO1
   gpio_free(gpioButton2);         // free the Button GPIO2
   printk(KERN_INFO "GPIO_TEST: Goodbye from the LKM!\n");
}

/** @brief The GPIO IRQ Handler function
 * A custom interrupt handler that is attached to the GPIO. The same
 * interrupt handler cannot be invoked concurrently as the line is
 * masked out until the function is complete. This function is static
 * as it should not be invoked directly from outside of this file.
 * @param irq    the IRQ number associated with the GPIO
 * @param dev_id the *dev_id that is provided - used to identify
 * which device caused the interrupt. Not used here.
 * @param regs   h/w specific register values -used for debugging.
 * return returns IRQ_HANDLED if successful - return IRQ_NONE otherwise.
 */
static irq_handler_t ebb_gpio_irq_handler1(unsigned int irq,
                        void *dev_id, struct pt_regs *regs){
   led1On = !led1On;                     // invert the LED state
   gpio_set_value(gpioLED1, led1On);     // set LED1 accordingly
   // gpio_set_value(gpioLED2, ledOn);     // set LED accordingly
   printk(KERN_INFO "GPIO_TEST: Interrupt! (button is %d)\n",
         gpio_get_value(gpioButton1));
   // printk(KERN_INFO "GPIO_TEST: Interrupt! (button is %d)\n",
   //       gpio_get_value(gpioButton2));
   numberPresses++;                    // global counter
   return (irq_handler_t) IRQ_HANDLED; // announce IRQ handled
}

/** @brief The GPIO IRQ Handler function
 * A custom interrupt handler that is attached to the GPIO. The same
 * interrupt handler cannot be invoked concurrently as the line is
 * masked out until the function is complete. This function is static
 * as it should not be invoked directly from outside of this file.
 * @param irq    the IRQ number associated with the GPIO
 * @param dev_id the *dev_id that is provided - used to identify
 * which device caused the interrupt. Not used here.
 * @param regs   h/w specific register values -used for debugging.
 * return returns IRQ_HANDLED if successful - return IRQ_NONE otherwise.
 */
static irq_handler_t ebb_gpio_irq_handler2(unsigned int irq,
                        void *dev_id, struct pt_regs *regs){
   led2On = !led2On;                     // invert the LED state
   // gpio_set_value(gpioLED1, ledOn);     // set LED1 accordingly
   gpio_set_value(gpioLED2, led2On);     // set LED accordingly
   // printk(KERN_INFO "GPIO_TEST: Interrupt! (button is %d)\n",
   //       gpio_get_value(gpioButton1));
   printk(KERN_INFO "GPIO_TEST: Interrupt! (button is %d)\n",
         gpio_get_value(gpioButton2));
   numberPresses++;                    // global counter
   return (irq_handler_t) IRQ_HANDLED; // announce IRQ handled
}

module_init(ebb_gpio_init);
module_exit(ebb_gpio_exit);
