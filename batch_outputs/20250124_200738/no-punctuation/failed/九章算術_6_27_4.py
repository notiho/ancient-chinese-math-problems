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
The total amount taxed across all five checkpoints is exactly 1 jin.
Question: how much gold did they originally carry?

The procedure says: Place 1 jin as the total taxed amount. 
Multiply it by the combined tax rates to obtain the dividend.
Also combine the untaxed portions and subtract them from the total to obtain the divisor.
Divide the dividend by the divisor to obtain the original amount of gold.

The answer says: *a* jin.
"""

from fractions import Fraction

# Tax rates at each checkpoint
稅率 = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 4), Fraction(1, 5), Fraction(1, 6)]

# Untaxed portions at each checkpoint
不稅率 = [1 - rate for rate in 稅率]

# Total taxed amount (1 jin)
總稅 = 1

# Combine taxed portions (通所稅者) and multiply by the total taxed amount
實 = 總稅
for rate in 稅率:
    實 *= rate

# Combine untaxed portions (通其不稅者) and subtract from 1 to get the divisor
法 = 1
for rate in 不稅率:
    法 *= rate

法 = 1 - 法

# Divide the dividend by the divisor to get the original amount of gold
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 1/600"""
