"""
今有粟三斗六升，欲為粺飯。問︰得幾何？
術曰：以粟求粺飯，二十七之，二十五而一。
荅曰：為粺飯 a斗 。
"""

#----- content starts here -----

# 粟三斗六升
粟 = 3 * 10 + 6  # 1斗 = 10升, 所以轉換為升

# 以粟求粺飯，二十七之
粺飯 = 27 * 粟

# 二十五而一
a = Fraction(粺飯, 25) / 10  # 轉換回斗 (1斗 = 10升)#----- content ends here -----

"""
"""
