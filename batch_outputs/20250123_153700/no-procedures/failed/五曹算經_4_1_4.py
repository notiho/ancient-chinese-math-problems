"""
今有官田九百畝凡一步收粟三升二合。問：計㡬何？
答曰： a斛 。
"""

"""
Suppose there is 900 mu of official land. For every bu of land, 3 sheng and 2 he of millet are harvested.
Question: how much millet is harvested in total?

Answer: *a* hu.
"""

from fractions import Fraction

# 官田九百畝
田地 = 900

# 每步收粟三升二合 (3 sheng and 2 he)
每步收粟 = 3 + Fraction(2, 10)  # Convert 2 he to fractional sheng (1 sheng = 10 he)

# 每畝有 240 步 (1 mu = 240 bu)
每畝步數 = 240

# 計算總收粟量 (in sheng)
總收粟量_升 = 每步收粟 * 每畝步數 * 田地

# 1 斛 = 10 升, convert sheng to hu
a = Fraction(總收粟量_升, 10)

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 6912, Actual: 69120"""
