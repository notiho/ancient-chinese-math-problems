"""
今有人持金出五關，前關二而稅一，次關三而稅一，次關四而稅一，次關五而稅一，次關六而稅一。并五關所稅，適重一斤。問︰本持金幾何？
術曰：置一斤，通所稅者以乘之為實。亦通其不稅者以減所通，餘為法。實如法得一斤。
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose a person carries gold through five checkpoints. 
At the first checkpoint, for every 2 jin, 1 jin is taxed.
At the second checkpoint, for every 3 jin, 1 jin is taxed.
At the third checkpoint, for every 4 jin, 1 jin is taxed.
At the fourth checkpoint, for every 5 jin, 1 jin is taxed.
At the fifth checkpoint, for every 6 jin, 1 jin is taxed.
The total tax collected across the five checkpoints is exactly 1 jin.
Question: how much gold did the person originally carry?

The procedure says: Place 1 jin [the total tax], and multiply it by the product of all the tax rates (the taxed portions) to obtain the dividend.
Also, subtract the product of all the untaxed portions from the product of all the tax rates to obtain the divisor.
Divide the dividend by the divisor to obtain the original amount of gold.

Answer: *a* jin.
"""

from fractions import Fraction

# Tax rates for each checkpoint
稅率1 = Fraction(1, 2)  # First checkpoint: 2 taxed, 1 kept
稅率2 = Fraction(1, 3)  # Second checkpoint: 3 taxed, 1 kept
稅率3 = Fraction(1, 4)  # Third checkpoint: 4 taxed, 1 kept
稅率4 = Fraction(1, 5)  # Fourth checkpoint: 5 taxed, 1 kept
稅率5 = Fraction(1, 6)  # Fifth checkpoint: 6 taxed, 1 kept

# Untaxed portions for each checkpoint
不稅率1 = 1 - 稅率1
不稅率2 = 1 - 稅率2
不稅率3 = 1 - 稅率3
不稅率4 = 1 - 稅率4
不稅率5 = 1 - 稅率5

# Total tax collected
總稅 = 1  # 1 jin

# 通所稅者以乘之為實
實 = 總稅 * 稅率1 * 稅率2 * 稅率3 * 稅率4 * 稅率5

# 亦通其不稅者以減所通，餘為法
法 = (稅率1 * 稅率2 * 稅率3 * 稅率4 * 稅率5) - (不稅率1 * 不稅率2 * 不稅率3 * 不稅率4 * 不稅率5)

# 實如法得一斤
a = Fraction(實, 法)
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6/5, Actual: -1/119"""
