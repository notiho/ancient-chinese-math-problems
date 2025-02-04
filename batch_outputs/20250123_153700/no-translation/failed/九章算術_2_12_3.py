"""
今有粟五斗、太半升，欲為麻。問︰得幾何？
術曰：以粟求菽、答、麻、麥，皆九之，十而一。
荅曰：為麻 a斗 。
"""


# 粟五斗、太半升
粟 = 5 + Fraction(1, 2) / 10  # Convert 太半升 to part of a 斗 (1斗 = 10升)

# 以粟求麻，皆九之
麻 = 9 * 粟

# 十而一
a = Fraction(麻, 10)  # Result in 斗
"""
Variable 'a' has wrong value. Expected: 114/25, Actual: 909/200"""
