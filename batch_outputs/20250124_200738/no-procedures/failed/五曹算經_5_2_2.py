"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
答曰： a銖 奇 b銖 。
"""

#----- content starts here -----
"""
Suppose there are 738 households in total, and they collectively request 27 jin and 5 liang of silk.
Question: how much silk does each household get?

Answer: each household gets *a* zhu and an additional *b* zhu.
"""

# Total number of households
households = 738

# Total silk requested: 27 jin and 5 liang
# 1 jin = 16 liang, so total silk in liang:
total_liang = 27 * 16 + 5

# Convert liang to zhu (1 liang = 24 zhu):
total_zhu = total_liang * 24

# Divide total zhu by the number of households to get the amount per household
silk_per_household = Fraction(total_zhu, households)

# Extract the integer part (a) and the remainder (b)
a = silk_per_household.numerator // silk_per_household.denominator
b = silk_per_household.numerator % silk_per_household.denominator

# Final result
a = Fraction(a)
b = Fraction(b, silk_per_household.denominator)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1421/100, Actual: 14
Variable 'b' has wrong value. Expected: 51/50, Actual: 26/123"""
