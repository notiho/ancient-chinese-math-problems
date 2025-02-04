"""
今有五百六十五户，共責絲八石五斤三两八銖。問：户出絲㡬何？
答曰： a斤 。
"""

#----- content starts here -----
"""
Suppose there are 565 households, and together they owe 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household contribute?

Answer: each household contributes *a* jin.
"""

# Total silk owed in smaller units (convert everything to zhu for calculation)
# 1 shi = 20 jin, 1 jin = 16 liang, 1 liang = 24 zhu
total_zhu = (8 * 20 * 16 * 24) + (5 * 16 * 24) + (3 * 24) + 8

# Number of households
households = 565

# Silk per household in zhu
silk_per_household_zhu = Fraction(total_zhu, households)

# Convert back to jin (1 jin = 16 liang, 1 liang = 24 zhu)
a_jin = silk_per_household_zhu // (16 * 24)  # Whole jin
remaining_zhu = silk_per_household_zhu % (16 * 24)

a_liang = remaining_zhu // 24  # Whole liang
remaining_zhu = remaining_zhu % 24

a_zhu = remaining_zhu  # Remaining zhu

# Final result
a = f"{a_jin}斤 {a_liang}两 {a_zhu}銖"#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 41/24, Actual: 0斤 4两 1840/113銖"""
