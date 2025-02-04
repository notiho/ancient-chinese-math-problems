"""
今有粟九斗八升，欲為大䵂。問︰得幾何？
術曰：以粟求大䵂，二十七之，二十五而一。
荅曰：為大䵂 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 9 dou and 8 sheng of millet. It is desired to turn it into daqu (a type of fermented grain).
Question: how much daqu is obtained?

The procedure says: when seeking daqu using millet, multiply by 27 and divide by 25.

The answer says: it makes *a* dou of daqu.
"""

# 粟九斗八升
粟斗 = 9
粟升 = 8

# Convert to total sheng (1 dou = 10 sheng)
粟總升 = (粟斗 * 10) + 粟升

# 以粟求大䵂，二十七之
大䵂 = 27 * 粟總升

# 二十五而一
大䵂斗 = Fraction(大䵂, 25)

# Convert back to dou (1 dou = 10 sheng)
a = Fraction(大䵂斗, 10)  # Result in dou#----- content ends here -----

"""
"""
