"""
今有粟九斗八升欲為大䵂問得幾何
術曰以粟求大䵂二十七之二十五而一
荅曰為大䵂 a斗 
"""

#----- content starts here -----
"""
Suppose there are 9 dou and 8 sheng of millet. It is desired to turn it into dafu (processed grain).
Question: how much dafu is obtained?

The procedure says: when seeking dafu using millet, multiply by 25 and divide by 27.

The answer says: it makes *a* dou of dafu.
"""

# 粟九斗八升
粟斗 = 9
粟升 = 8

# Convert everything to 升 (1 斗 = 10 升)
粟 = 10 * 粟斗 + 粟升

# 以粟求大䵂，二十七之二十五
大䵂 = 25 * 粟

# 而一，除以 27
大䵂 = Fraction(大䵂, 27)

# Convert back to 斗 (1 斗 = 10 升)
a = Fraction(大䵂, 10)  # Result in dou#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1323/125, Actual: 245/27"""
