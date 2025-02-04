"""
今有人持金出五關前關二而稅一次關三而稅一次關四而稅一次關五而稅一次關六而稅一并五關所稅適重一斤問本持金幾何
術曰置一斤通所稅者以乘之為實亦通其不稅者以減所通餘為法實如法得一斤
荅曰 a斤 
"""

#----- content starts here -----
"""
Suppose a person carries gold through five checkpoints.
At the first checkpoint, 2 is the divisor for taxation.
At the second checkpoint, 3 is the divisor for taxation.
At the third checkpoint, 4 is the divisor for taxation.
At the fourth checkpoint, 5 is the divisor for taxation.
At the fifth checkpoint, 6 is the divisor for taxation.
The total tax collected at all five checkpoints equals exactly 1 jin.
Question: how much gold did the person originally carry?

The procedure says: Place 1 jin as the total tax collected.
Multiply it by the product of all the divisors (including those that do not tax), obtaining the dividend.
Also multiply the product of all the divisors that do not tax, and subtract it from the total product, obtaining the divisor.
Divide the dividend by the divisor to obtain the original amount of gold.

The answer says: *a* jin.
"""

# 稅率
稅率 = [2, 3, 4, 5, 6]

# 置一斤通所稅者
總稅 = 1

# 以乘之為實
實 = 總稅
for rate in 稅率:
    實 *= rate

# 亦通其不稅者以減所通餘為法
法 = 1
for rate in 稅率:
    法 *= rate
for rate in 稅率:
    法 -= 法 // rate

# 實如法得一斤
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 6"""
