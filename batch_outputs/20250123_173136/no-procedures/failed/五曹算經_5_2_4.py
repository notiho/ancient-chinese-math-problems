"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
答曰： a銖 奇 b銖 。
"""

"""
Suppose there are 738 households, and together they request 27 jin and 5 liang of silk.
Question: how much silk does each household get?

Answer: each household gets *a* zhu and an additional *b* zhu.
"""

# Total silk in jin and liang
total_jin = 27
total_liang = 5

# Conversion factors
jin_to_liang = 16  # 1 jin = 16 liang
liang_to_zhu = 24  # 1 liang = 24 zhu

# Convert total silk to zhu
total_zhu = (total_jin * jin_to_liang + total_liang) * liang_to_zhu

# Number of households
households = 738

# Divide total zhu by households to find how much each household gets
silk_per_household = Fraction(total_zhu, households)

# Extract the integer part (a) and the remainder (b)
a = silk_per_household.numerator // silk_per_household.denominator
b = silk_per_household.numerator % silk_per_household.denominator

# Final result
a = Fraction(a)
b = Fraction(b, silk_per_household.denominator)
"""
Variable 'a' has wrong value. Expected: 1421/100, Actual: 14
Variable 'b' has wrong value. Expected: 51/50, Actual: 26/123"""
