"""
今有粟五斗五升，欲為飧。問︰得幾何？
術曰：以粟求飧，九之，五而一。
荅曰：為飧 a斗 。
"""

#----- content starts here -----

# 粟五斗五升
粟 = 5 + Fraction(5, 10)  # 1斗 = 10升

# 以粟求飧，九之
飧 = 9 * 粟

# 五而一
a = Fraction(飧, 5)  # 答案以斗為單位#----- content ends here -----

"""
"""
