"""
今有粟五斗、太半升，欲為麻。問︰得幾何？
術曰：以粟求菽、答、麻、麥，皆九之，十而一。
荅曰：為麻 a斗 。
"""

#----- content starts here -----

# 粟五斗、太半升
粟 = 5 + Fraction(1, 2)  # 5斗 + 太半升 (1/2斗)

# 以粟求麻，皆九之
麻 = 9 * 粟

# 十而一
a = Fraction(麻, 10)  # 得麻 a斗#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 114/25, Actual: 99/20"""
