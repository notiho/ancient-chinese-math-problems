"""
今有粟四斗一升、太半升，欲為答。問︰得幾何？
術曰：以粟求菽、答、麻、麥，皆九之，十而一。
荅曰：為答 a斗 。
"""

#----- content starts here -----

# 粟四斗一升、太半升
粟 = 4 * 10 + 1 + Fraction(1, 2)  # 1斗 = 10升

# 以粟求答，皆九之
答 = 9 * 粟

# 十而一
a = Fraction(答, 10)  # Convert to 答 in 斗

#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 15/4, Actual: 747/20"""
