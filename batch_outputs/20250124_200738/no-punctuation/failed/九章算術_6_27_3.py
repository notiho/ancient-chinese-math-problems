"""
今有人持金出五關前關二而稅一次關三而稅一次關四而稅一次關五而稅一次關六而稅一并五關所稅適重一斤問本持金幾何
術曰置一斤通所稅者以乘之為實亦通其不稅者以減所通餘為法實如法得一斤
荅曰 a斤 
"""

#----- content starts here -----
"""
Suppose a person carries gold through five checkpoints. 
At the first checkpoint, 1/2 is taxed; at the second checkpoint, 1/3 is taxed; at the third checkpoint, 1/4 is taxed; at the fourth checkpoint, 1/5 is taxed; and at the fifth checkpoint, 1/6 is taxed.
The total tax from all five checkpoints equals exactly 1 jin.
Question: how much gold did the person originally carry?

The procedure says: Place 1 jin as the total tax.
Multiply it by the combined taxed portions, obtaining the dividend.
Also combine the untaxed portions, subtracting from 1 to obtain the divisor.
Divide the dividend by the divisor to obtain the original amount of gold.

The answer says: *a* jin.
"""

# 稅率 for each checkpoint
稅率 = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 4), Fraction(1, 5), Fraction(1, 6)]

# 置一斤通所稅者
總稅 = 1

# 通所稅者以乘之，為實
實 = 總稅

# 通其不稅者，以減所通
不稅率 = [1 - 稅 for 稅 in 稅率]
法 = 1
for 不稅 in 不稅率:
    法 *= 不稅

# 實如法得一斤
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 6"""
