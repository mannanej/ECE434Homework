tempSet='i2cset -y 2 0x49 2 0x00'
tempSet2='i2cset -y 2 0x49 3 0x1a'

temp=`i2cget -y 2 0x49`
echo $temp
temp2=$((( $temp * 9 ) / 5 + 32 ))
echo $temp2