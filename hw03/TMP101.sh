tempSet='i2cset -y 2 0x49 2 0x00'
tempSet2='i2cset -y 2 0x49 3 0x1a'

temp=`i2cget -y 2 0x49`
temp1=`i2cget -y 2 0x48`
# echo $temp
# echo $temp1
temp2=$((( $temp * 9 ) / 5 + 32 ))
temp12=$((( $temp1 * 9 ) / 5 + 32 ))
echo $temp2
echo $temp12