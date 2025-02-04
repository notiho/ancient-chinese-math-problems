"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
答曰： a銖 奇 b銖 。
"""

"""
Suppose there are 738 households, and together they request 27 jin and 5 liang of silk.
Question: how much silk does each household get?

Answer: each household gets *a* zhu and an additional *b* zhu.
"""

# Total number of households
households = 738

# Total silk in jin and liang
total_silk_jin = 27
total_silk_liang = 5

# Convert jin and liang to zhu
# 1 jin = 16 liang, 1 liang = 24 zhu
total_silk_zhu = (total_silk_jin * 16 + total_silk_liang) * 24

# Divide total silk by the number of households
silk_per_household = Fraction(total_silk_zhu, households)

# Extract the integer part (a) and the remainder (b)
a = silk_per_household.numerator // silk_per_household.denominator
b = silk_per_household.numerator % silk_per_household.denominator

# Final result
a, b
"""
Variable 'a' has wrong value. Expected: 1421/100, Actual: 14
Variable 'b' has wrong value. Expected: 51/50, Actual: 26"""
