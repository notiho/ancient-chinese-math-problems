"""
今有五百六十五户，共責絲八石五斤三两八銖。問：户出絲㡬何？
答曰： a斤 b 两 c銖 。
"""

"""
Suppose there are 565 households, and together they owe 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household contribute?

Answer: each household contributes *a* jin, *b* liang, and *c* zhu.
"""

# Total silk owed in smaller units
# 1 shi = 120 jin, 1 jin = 16 liang, 1 liang = 24 zhu
total_silk_in_zhu = (8 * 120 * 16 * 24) + (5 * 16 * 24) + (3 * 24) + 8

# Number of households
households = 565

# Silk per household in zhu
silk_per_household_in_zhu = Fraction(total_silk_in_zhu, households)

# Convert zhu to jin, liang, and zhu
a = silk_per_household_in_zhu // (16 * 24)  # jin
remaining_zhu = silk_per_household_in_zhu % (16 * 24)

b = remaining_zhu // 24  # liang
c = remaining_zhu % 24  # zhu

a, b, c  # Output the result as a jin, b liang, c zhu
"""
"""
