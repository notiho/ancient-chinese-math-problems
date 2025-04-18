"""
今有粟九斗八升，欲為御飯。問︰得幾何？
術曰：以粟求御飯，二十一之，二十五而一。
荅曰：為御飯 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 9 dou and 8 sheng of millet. It is desired to turn it into cooked rice.
Question: how much cooked rice does it make?

The procedure says: when seeking cooked rice using millet, multiply by 21 and divide by 25.

The answer says: it makes *a* dou of cooked rice.
"""

# 粟九斗八升
粟斗 = 9
粟升 = 8

# Convert to total sheng (1 dou = 10 sheng)
粟總升 = (粟斗 * 10) + 粟升

# 以粟求御飯，二十一之
御飯 = 21 * 粟總升

# 二十五而一
御飯總升 = Fraction(御飯, 25)

# Convert back to dou and sheng
御飯斗 = 御飯總升 // 10  # Whole dou
御飯升 = 御飯總升 % 10   # Remaining sheng

a = Fraction(御飯總升, 10)  # Final answer in dou#----- content ends here -----

"""
"""
