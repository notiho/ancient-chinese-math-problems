"""
今有人持金出五關，前關二而稅一，次關三而稅一，次關四而稅一，次關五而稅一，次關六而稅一。并五關所稅，適重一斤。問︰本持金幾何？
術曰：置一斤，通所稅者以乘之為實。亦通其不稅者以減所通，餘為法。實如法得一斤。
荅曰： a(=6/5)斤 。
"""

"""
Suppose a person carries gold through five checkpoints.
At the first checkpoint, for every 2 jin, 1 jin is taxed.
At the second checkpoint, for every 3 jin, 1 jin is taxed.
At the third checkpoint, for every 4 jin, 1 jin is taxed.
At the fourth checkpoint, for every 5 jin, 1 jin is taxed.
At the fifth checkpoint, for every 6 jin, 1 jin is taxed.
The total tax across all five checkpoints equals exactly 1 jin.
Question: how much gold did the person originally carry?

The procedure says: Place 1 jin as the total tax.
Multiply it by the product of all the tax rates to obtain the dividend.
Also, subtract the product of all the non-taxed parts from the total product to obtain the divisor.
Divide the dividend by the divisor to obtain the original amount of gold.

Answer: *a*(=6/5) jin.
"""

# 稅率
稅率 = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 4), Fraction(1, 5), Fraction(1, 6)]

# 通所稅者 (稅率的分子相乘)
通所稅 = 1
for 稅 in 稅率:
    通所稅 *= 稅.numerator

# 通其不稅者 (稅率的分母相乘)
通不稅 = 1
for 稅 in 稅率:
    通不稅 *= 稅.denominator

# 減所通，餘為法
法 = 通不稅 - 通所稅

# 置一斤，通所稅者以乘之為實
實 = 通所稅 * 1

# 實如法得一斤
a = Fraction(實, 法) # 6/5

"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 1/719"""
