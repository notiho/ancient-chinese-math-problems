"""
今有人持金出五關，前關二而稅一，次關三而稅一，次關四而稅一，次關五而稅一，次關六而稅一。并五關所稅，適重一斤。問︰本持金幾何？
術曰：置一斤，通所稅者以乘之為實。亦通其不稅者以減所通，餘為法。實如法得一斤。
荅曰： a斤 。
"""

#----- content starts here -----

# 前關稅率
稅率 = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 4), Fraction(1, 5), Fraction(1, 6)]

# 置一斤
稅總 = 1

# 通所稅者以乘之為實
實 = 稅總
for 稅 in 稅率:
    實 *= (1 + 稅)

# 亦通其不稅者以減所通，餘為法
法 = 1
for 稅 in 稅率:
    法 *= (1 - 稅)

# 實如法得一斤
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 21"""
