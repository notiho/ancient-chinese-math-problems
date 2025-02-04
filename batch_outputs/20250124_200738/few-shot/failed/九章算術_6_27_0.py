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
The total tax across all five checkpoints is exactly 1 jin.
Question: how much gold did the person originally carry?

The procedure says: Place 1 jin (the total tax), and multiply it by the total taxed proportions to obtain the dividend.
Also, subtract the total untaxed proportions from the total taxed proportions to obtain the divisor.
Divide the dividend by the divisor to obtain the original amount of gold.

Answer: *a* jin.
"""

# 前關二而稅一
前關稅率 = Fraction(1, 2)

# 次關三而稅一
次關稅率1 = Fraction(1, 3)

# 次關四而稅一
次關稅率2 = Fraction(1, 4)

# 次關五而稅一
次關稅率3 = Fraction(1, 5)

# 次關六而稅一
次關稅率4 = Fraction(1, 6)

# 通所稅者
通所稅 = 前關稅率 + 次關稅率1 + 次關稅率2 + 次關稅率3 + 次關稅率4

# 通其不稅者
通其不稅 = (1 - 前關稅率) * (1 - 次關稅率1) * (1 - 次關稅率2) * (1 - 次關稅率3) * (1 - 次關稅率4)

# 餘為法
法 = 通所稅 - 通其不稅

# 置一斤
稅 = 1

# 通所稅者以乘之為實
實 = 稅 * 通所稅

# 實如法得一斤
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 87/77"""
