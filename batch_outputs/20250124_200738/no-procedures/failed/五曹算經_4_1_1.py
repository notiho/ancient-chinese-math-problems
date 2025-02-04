"""
今有官田九百畝凡一步收粟三升二合。問：計㡬何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is 900 mu of official land, and for every bu of land, 3 sheng and 2 he of millet are harvested.
Question: how much millet is harvested in total?

Answer: *a* hu.
"""

from fractions import Fraction

# 官田九百畝
官田 = 900

# 每步收粟三升二合 (3 sheng and 2 he)
# 1 sheng = 10 he, so 3 sheng 2 he = 3 + 2/10 = 32/10 sheng
每步收粟 = Fraction(32, 10)

# 1 畝 = 240 步
每畝步數 = 240

# Total millet harvested in sheng
總收粟升 = 官田 * 每畝步數 * 每步收粟

# Convert sheng to hu (1 hu = 10 sheng)
a = 總收粟升 / 10

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6912, Actual: 69120"""
