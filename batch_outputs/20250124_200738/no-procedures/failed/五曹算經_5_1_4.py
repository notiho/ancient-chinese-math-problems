"""
今有五百六十五户，共責絲八石五斤三两八銖。問：户出絲㡬何？
答曰： a斤 。
"""

#----- content starts here -----
"""
Suppose there are 565 households, and together they owe 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household owe?

Answer: each household owes *a* jin of silk.
"""

# Total silk owed in units of jin
# 1 shi = 100 jin, 1 jin = 16 liang, 1 liang = 24 zhu
total_silk_in_jin = 8 * 100 + 5 + Fraction(3, 16) + Fraction(8, 16 * 24)

# Number of households
households = 565

# Silk owed per household
a = total_silk_in_jin / households

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 41/24, Actual: 3865/2712"""
