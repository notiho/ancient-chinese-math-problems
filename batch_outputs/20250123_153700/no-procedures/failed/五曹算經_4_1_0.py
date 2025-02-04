"""
今有官田九百畝凡一步收粟三升二合。問：計㡬何？
答曰： a斛 。
"""

"""
Suppose there is 900 mu of official land, and for every bu of land, 3 sheng and 2 he of millet are harvested.
Question: how much millet is harvested in total?

Answer: *a* hu.
"""

from fractions import Fraction

# 官田九百畝
官田 = 900

# 每畝有 240 步 (1 mu = 240 bu)
每畝步數 = 240

# 每步收粟 3 升 2 合 (1 升 = 10 合, so 3 升 2 合 = 3 + 2/10 = 32/10 升)
每步收粟 = Fraction(32, 10)  # in sheng

# 每畝收粟 = 每步收粟 * 每畝步數
每畝收粟 = 每步收粟 * 每畝步數  # in sheng

# 總收粟 = 每畝收粟 * 官田
總收粟 = 每畝收粟 * 官田  # in sheng

# 1 斛 = 10 升, so convert sheng to hu
a = 總收粟 / 10  # in hu

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 6912, Actual: 69120"""
