"""
今有粟九斗八升欲為大䵂問得幾何
術曰以粟求大䵂二十七之二十五而一
荅曰為大䵂 a斗 
"""

#----- content starts here -----
"""
Suppose there are 9 dou and 8 sheng of millet. It is desired to turn it into dafu (processed grain).
Question: how much dafu is obtained?

The procedure says: When seeking dafu from millet, multiply by 25 and divide by 27.

The answer says: it makes *a* dou of dafu.
"""

# 粟九斗八升
粟斗 = 9
粟升 = 8

# Convert to total sheng (1 dou = 10 sheng)
粟總升 = 10 * 粟斗 + 粟升

# 以粟求大䵂，二十七之二十五
大䵂總升 = Fraction(25 * 粟總升, 27)

# Convert back to dou and sheng
a斗 = 大䵂總升 // 10  # Whole dou
a升 = 大䵂總升 % 10   # Remaining sheng

a = Fraction(a斗) + Fraction(a升, 10)  # Final result in dou#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1323/125, Actual: 245/27"""
