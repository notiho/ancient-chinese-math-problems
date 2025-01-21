"""
今有五百六十五户，共責絲八石五斤三两八銖。問：户出絲㡬何？
答曰： a斤 b 两 c銖 。
"""

"""
Suppose there are 565 households, and together they owe 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household contribute?

Answer: Each household contributes *a* jin, *b* liang, and *c* zhu.
"""

# Total households
households = 565

# Total silk owed
shi_to_jin = 8 * 120  # 1 shi = 120 jin
jin = shi_to_jin + 5  # Add the 5 jin
liang = 3  # 1 jin = 16 liang
zhu = 8  # 1 liang = 24 zhu

# Convert everything to zhu for easier calculation
total_zhu = (jin * 16 * 24) + (liang * 24) + zhu

# Divide total zhu by the number of households
zhu_per_household = Fraction(total_zhu, households)

# Convert back to jin, liang, and zhu
jin_per_household = zhu_per_household // (16 * 24)
remaining_zhu = zhu_per_household % (16 * 24)

liang_per_household = remaining_zhu // 24
zhu_per_household = remaining_zhu % 24

# Final result
a = jin_per_household
b = liang_per_household
c = zhu_per_household

a, b, c  # Output the result as (a jin, b liang, c zhu) per household
"""
"""
