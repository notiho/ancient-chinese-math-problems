"""
今有官田九百畝凡一步收粟三升二合。問：計㡬何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 900 mu of official land, and each bu of land produces 3 sheng and 2 he of millet.
Question: how much millet is produced in total?

Answer: *a* hu.
"""

from fractions import Fraction

# 官田九百畝
田地 = 900

# 每步收粟三升二合 (3 sheng and 2 he per bu)
每步收粟 = 3 + Fraction(2, 10)  # 1 sheng = 10 he

# 每畝有240步 (1 mu = 240 bu)
每畝步數 = 240

# 總粟量 (in sheng)
總粟量 = 每步收粟 * 每畝步數 * 田地

# Convert sheng to hu (1 hu = 10 sheng)
a = Fraction(總粟量, 10)

a  # Output the total amount of millet in hu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6912, Actual: 69120"""
