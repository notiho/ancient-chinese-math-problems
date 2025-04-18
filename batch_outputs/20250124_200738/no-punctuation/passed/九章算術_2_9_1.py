"""
今有粟九斗八升欲為御飯問得幾何
術曰以粟求御飯二十一之二十五而一
荅曰為御飯 a斗 
"""

#----- content starts here -----
"""
Suppose there are 9 dou and 8 sheng of millet. It is desired to turn it into cooked rice.
Question: how much cooked rice does it make?

The procedure says: When seeking cooked rice using millet, multiply by 21 and divide by 25.

The answer says: it makes *a* dou of cooked rice.
"""

# 粟九斗八升
粟斗 = 9
粟升 = 8

# Convert everything to 升 (1 斗 = 10 升)
粟總升 = (粟斗 * 10) + 粟升

# 以粟求御飯，二十一之
御飯升 = 21 * 粟總升

# 二十五而一
御飯總升 = Fraction(御飯升, 25)

# Convert back to 斗 and 升
御飯斗 = 御飯總升 // 10  # Whole dou
御飯升 = 御飯總升 % 10   # Remaining sheng

a = Fraction(御飯斗) + Fraction(御飯升, 10)  # Final result in dou
#----- content ends here -----

"""
"""
