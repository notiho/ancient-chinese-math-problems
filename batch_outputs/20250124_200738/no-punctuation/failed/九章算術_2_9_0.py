"""
今有粟九斗八升欲為御飯問得幾何
術曰以粟求御飯二十一之二十五而一
荅曰為御飯 a斗 
"""

#----- content starts here -----
"""
Suppose there are 9 dou and 8 sheng of millet. It is desired to turn it into cooked rice.
Question: how much cooked rice does one obtain?

The procedure says: when seeking cooked rice from millet, multiply by 21 and divide by 25.

The answer says: it makes *a* dou of cooked rice.
"""

# 粟九斗八升
粟斗 = 9
粟升 = 8

# Convert everything to 升 (1 斗 = 10 升)
粟 = (粟斗 * 10) + 粟升

# 以粟求御飯，二十一之
御飯 = 21 * 粟

# 二十五而一
a = Fraction(御飯, 25)

# Convert back to 斗 (1 斗 = 10 升)
a斗 = a // 10  # Whole dou
a升 = a % 10   # Remaining sheng

a = f"{a斗}斗 {a升}升"  # Final result in dou and sheng#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1029/125, Actual: 8斗 58/25升"""
