"""
今有五百六十五户，共責絲八石五斤三两八銖。問：户出絲㡬何？
答曰： a斤 b 两 c銖 。
"""

"""
Suppose there are 565 households, and together they owe 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household owe?

Answer: each household owes *a* jin, *b* liang, and *c* zhu.
"""

# Total households
households = 565

# Total silk owed
shi = 8  # 1 shi = 100 jin
jin = 5  # 1 jin = 16 liang
liang = 3  # 1 liang = 24 zhu
zhu = 8

# Convert everything to zhu for calculation
total_zhu = (shi * 100 * 16 * 24) + (jin * 16 * 24) + (liang * 24) + zhu

# Divide total zhu by the number of households
silk_per_household_zhu = Fraction(total_zhu, households)

# Convert back to jin, liang, and zhu
a = silk_per_household_zhu // (16 * 24)  # jin
remaining_zhu = silk_per_household_zhu % (16 * 24)

b = remaining_zhu // 24  # liang
c = remaining_zhu % 24  # zhu

# Final result: a jin, b liang, c zhu
a, b, c
"""
Variable 'b' has wrong value. Expected: 11, Actual: 6
Variable 'c' has wrong value. Expected: 8, Actual: 2176/113"""
