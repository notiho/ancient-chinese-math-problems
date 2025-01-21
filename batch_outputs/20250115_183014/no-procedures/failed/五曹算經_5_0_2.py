"""
今有五百六十五户，户責絲一斤十一两八銖。問：計絲㡬何？
答曰： a石 b 两 c銖 。
"""

"""
Suppose there are 565 households, and each household owes 1 jin, 11 liang, and 8 zhu of silk.
Question: how much silk is owed in total?

Answer: *a* shi, *b* liang, and *c* zhu.
"""

# Define the number of households
households = 565

# Define the amount of silk owed per household
jin_per_household = 1  # 1 jin
liang_per_household = 11  # 11 liang
zhu_per_household = 8  # 8 zhu

# Conversion factors
liang_per_jin = 16  # 1 jin = 16 liang
zhu_per_liang = 24  # 1 liang = 24 zhu
liang_per_shi = 160  # 1 shi = 10 jin = 160 liang

# Convert the owed silk per household entirely into zhu
silk_per_household_in_zhu = (
    jin_per_household * liang_per_jin * zhu_per_liang
    + liang_per_household * zhu_per_liang
    + zhu_per_household
)

# Calculate the total silk owed in zhu
total_silk_in_zhu = households * silk_per_household_in_zhu

# Convert the total silk into shi, liang, and zhu
a = total_silk_in_zhu // (liang_per_shi * zhu_per_liang)  # shi
remaining_zhu = total_silk_in_zhu % (liang_per_shi * zhu_per_liang)

b = remaining_zhu // zhu_per_liang  # liang
c = remaining_zhu % zhu_per_liang  # zhu

# Final result: a shi, b liang, c zhu
a, b, c
"""
Variable 'a' has wrong value. Expected: 193/24, Actual: 96
Variable 'b' has wrong value. Expected: 3, Actual: 83"""
