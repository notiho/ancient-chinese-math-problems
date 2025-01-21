"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
答曰： a銖 b 絫 c黍 奇 d銖 e黍 。
"""

"""
Suppose there are 738 households, and together they request 27 jin and 5 liang of silk.
Question: how much does each household receive?

Answer: each household receives *a* zhu, *b* lü, *c* shu, with a remainder of *d* zhu and *e* shu.
"""

### Units Conversion ###
# 1 jin = 16 liang
# 1 liang = 24 zhu
# 1 zhu = 100 shu

# Total silk in jin, liang, zhu, and shu
total_jin = 27
total_liang = 5

# Convert everything to shu
total_shu = (total_jin * 16 * 24 * 100) + (total_liang * 24 * 100)

# Number of households
households = 738

# Silk per household in shu
silk_per_household = total_shu // households
remainder_shu = total_shu % households

# Convert silk per household back to jin, liang, zhu, and shu
a = silk_per_household // (24 * 100)  # zhu
b = (silk_per_household % (24 * 100)) // 100  # lü
c = (silk_per_household % 100)  # shu

# Remainder in zhu and shu
d = remainder_shu // 100  # zhu
e = remainder_shu % 100  # shu

a, b, c, d, e
"""
Variable 'a' has wrong value. Expected: 14, Actual: 0
Variable 'b' has wrong value. Expected: 2, Actual: 14
Variable 'c' has wrong value. Expected: 1, Actual: 21"""
