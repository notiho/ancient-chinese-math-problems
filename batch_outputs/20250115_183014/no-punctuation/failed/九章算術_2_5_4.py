"""
今有粟九斗八升欲為大䵂問得幾何
術曰以粟求大䵂二十七之二十五而一
荅曰為大䵂 a斗 
"""

"""
Suppose there are 9 dou and 8 sheng of millet. It is desired to turn it into dafu (processed grain).
Question: how much dafu does one obtain?

The procedure says: when seeking dafu from millet, multiply by 25 and divide by 27.

The answer says: it makes *a* dou of dafu.
"""

# 粟九斗八升
粟斗 = 9
粟升 = 8

# Convert everything to 升 (1 dou = 10 sheng)
粟 = 10 * 粟斗 + 粟升

# 以粟求大䵂，二十七之二十五
大䵂 = 25 * 粟

# 而一
a = Fraction(大䵂, 27)

# Convert back to dou (1 dou = 10 sheng)
a斗 = a // 10  # Whole dou
a升 = a % 10   # Remaining sheng

a = f"{a斗}斗 {a升}升"
"""
Variable 'a' has wrong value. Expected: 1323/125, Actual: 9斗 20/27升"""
