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
官田 = 900

# 每步收粟三升二合 (3 sheng and 2 he)
# Convert 3 sheng 2 he into a single unit in terms of sheng
# 1 sheng = 10 he
每步收粟 = 3 + Fraction(2, 10)

# 每畝有 240 步
每畝步數 = 240

# 計算總收穫量 (in sheng)
總收穫量_升 = 官田 * 每畝步數 * 每步收粟

# Convert sheng to hu
# 1 hu = 10 sheng
a = Fraction(總收穫量_升, 10)

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 6912, Actual: 69120"""
