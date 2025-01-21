"""
今有人持金出五關，前關二而稅一，次關三而稅一，次關四而稅一，次關五而稅一，次關六而稅一。并五關所稅，適重一斤。問︰本持金幾何？
術曰：置一斤，通所稅者以乘之為實。亦通其不稅者以減所通，餘為法。實如法得一斤。
荅曰： a斤 。
"""

"""
Suppose a person carries gold through five checkpoints.
At the first checkpoint, for every 2 jin, 1 jin is taxed.
At the second checkpoint, for every 3 jin, 1 jin is taxed.
At the third checkpoint, for every 4 jin, 1 jin is taxed.
At the fourth checkpoint, for every 5 jin, 1 jin is taxed.
At the fifth checkpoint, for every 6 jin, 1 jin is taxed.
The total tax across the five checkpoints is exactly 1 jin.
Question: how much gold did the person originally carry?

The procedure says: Place 1 jin as the total tax.
Multiply it by the combined tax rates to obtain the dividend.
Also combine the untaxed portions and subtract them from the total combined portions to obtain the divisor.
Divide the dividend by the divisor to obtain the original amount of gold.

Answer: *a* jin.
"""

# 前關二而稅一
前關稅率 = Fraction(1, 2)

# 次關三而稅一
次關稅率_1 = Fraction(1, 3)

# 次關四而稅一
次關稅率_2 = Fraction(1, 4)

# 次關五而稅一
次關稅率_3 = Fraction(1, 5)

# 次關六而稅一
次關稅率_4 = Fraction(1, 6)

# 通所稅者以乘之為實
通稅率 = 前關稅率 + 次關稅率_1 + 次關稅率_2 + 次關稅率_3 + 次關稅率_4
實 = 1  # Total tax is 1 jin

# 亦通其不稅者以減所通，餘為法
通不稅率 = (1 - 前關稅率) * (1 - 次關稅率_1) * (1 - 次關稅率_2) * (1 - 次關稅率_3) * (1 - 次關稅率_4)
法 = 1 - 通不稅率

# 實如法得一斤
a = Fraction(實, 法)
"""
"""
