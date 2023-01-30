from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chromeOptions = Options()
# chromeOptions.headless = True
chromeOptions.add_argument("--headless")
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("--window-size=1280,720")
chromeOptions.add_argument("—disable-gpu")
# browser = webdriver.Chrome(executable_path="~/ECE434Homework/FinalProjectTesting/drivers/chromedriver", options=chromeOptions)
# browser = webdriver.Chrome(service = Service("./drivers/chromedriver"), options=chromeOptions)
browser = webdriver.Chrome(service = Service("~/ECE434Homework/FinalProjectTesting/drivers/chromedriver"), options=chromeOptions)
browser.get("http://linuxhint.com")
print("Title: %s" % browser.title)
browser.quit()