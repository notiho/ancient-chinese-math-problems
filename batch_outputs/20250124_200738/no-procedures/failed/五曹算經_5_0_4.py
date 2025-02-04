"""
今有五百六十五户，户責絲一斤十一两八銖。問：計絲㡬何？
答曰： a石 。
"""

#----- content starts here -----
"""
Suppose there are 565 households, and each household owes 1 jin, 11 liang, and 8 zhu of silk.
Question: how much silk is owed in total?

Answer: *a* shi.
"""

# Total households
households = 565

# Silk owed per household: 1 jin, 11 liang, 8 zhu
# 1 jin = 16 liang, 1 liang = 24 zhu
silk_per_household = 1 * 16 * 24 + 11 * 24 + 8  # Convert everything to zhu

# Total silk owed in zhu
total_silk_in_zhu = households * silk_per_household

# Convert total silk to shi
# 1 shi = 20 jin = 20 * 16 * 24 zhu
zhu_per_shi = 20 * 16 * 24
a = Fraction(total_silk_in_zhu, zhu_per_shi)

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4633/576, Actual: 4633/96"""
