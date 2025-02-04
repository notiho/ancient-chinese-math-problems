"""
今有人持金出五關前關二而稅一次關三而稅一次關四而稅一次關五而稅一次關六而稅一并五關所稅適重一斤問本持金幾何
術曰置一斤通所稅者以乘之為實亦通其不稅者以減所通餘為法實如法得一斤
荅曰 a斤 
"""

#----- content starts here -----
"""
Suppose someone carries gold through five checkpoints. 
At the first checkpoint, they are taxed 1/2 of their gold.
At the second checkpoint, they are taxed 1/3 of their gold.
At the third checkpoint, they are taxed 1/4 of their gold.
At the fourth checkpoint, they are taxed 1/5 of their gold.
At the fifth checkpoint, they are taxed 1/6 of their gold.
The total tax collected across all five checkpoints is exactly 1 jin.
Question: how much gold did they originally carry?

The procedure says: Place 1 jin as the total tax collected.
Multiply it by the combined tax rates, obtaining the dividend.
Also combine the non-taxed portions, subtracting from 1 to obtain the divisor.
Divide the dividend by the divisor to obtain the original amount of gold.

Answer: *a* jin.
"""

from fractions import Fraction

# 置一斤通所稅者
稅總 = 1

# 稅率：二而稅一次，三而稅一次，四而稅一次，五而稅一次，六而稅一次
稅率 = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 4), Fraction(1, 5), Fraction(1, 6)]

# 通所稅者以乘之，為實
實 = 稅總
for 稅 in 稅率:
    實 *= (1 + 稅)

# 通其不稅者以減，所通餘為法
法 = 1
for 稅 in 稅率:
    法 *= (1 - 稅)

# 實如法得一斤
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 21"""
