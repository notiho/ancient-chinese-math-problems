"""
今有粟九斗八升，欲為大䵂。問︰得幾何？
術曰：以粟求大䵂，二十七之，二十五而一。
荅曰：為大䵂 a斗 。
"""

#----- content starts here -----

# 粟九斗八升
粟 = 9 * 10 + 8  # 1斗 = 10升, so convert to 升

# 以粟求大䵂，二十七之
大䵂 = 27 * 粟

# 二十五而一
a = Fraction(大䵂, 25) / 10  # Convert back to 斗 (1斗 = 10升)#----- content ends here -----

"""
"""
