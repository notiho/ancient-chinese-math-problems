"""
今有粟三斗少半升，欲為菽。問︰得幾何？
術曰：以粟求菽、答、麻、麥，皆九之，十而一。
荅曰：為菽 a斗 。
"""

#----- content starts here -----

# 粟三斗少半升
粟 = 3 + Fraction(1, 20)  # 1斗 = 10升, 半升 = 1/20斗

# 以粟求菽，皆九之
菽 = 9 * 粟

# 十而一
a = Fraction(菽, 10)  # 得到菽的數量#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 273/100, Actual: 549/200"""
