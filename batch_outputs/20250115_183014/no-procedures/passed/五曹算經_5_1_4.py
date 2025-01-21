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
# 1 石 = 120 斤, 1 斤 = 16 两, 1 两 = 24 銖
total_silk_in_zhu = (8 * 120 * 16 * 24) + (5 * 16 * 24) + (3 * 24) + 8

# Silk owed per household in zhu
silk_per_household_in_zhu = Fraction(total_silk_in_zhu, households)

# Convert zhu to jin, liang, and zhu
a = silk_per_household_in_zhu // (16 * 24)  # Jin
remaining_zhu = silk_per_household_in_zhu % (16 * 24)

b = remaining_zhu // 24  # Liang
c = remaining_zhu % 24  # Zhu

a, b, c  # Output the result in jin, liang, and zhu
"""
"""
