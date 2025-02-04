"""
今有粟八斗六升欲為鑿飯問得幾何
術曰以粟求鑿飯二十四之二十五而一
荅曰為鑿飯 a斗 
"""

"""
Suppose there are 8 dou and 6 sheng of millet. It is desired to turn it into cooked rice.
Question: how much cooked rice does it make?

The procedure says: when seeking cooked rice from millet, multiply by 25 and divide by 24.

The answer says: it makes *a* dou of cooked rice.
"""

# 粟八斗六升
粟斗 = 8
粟升 = 6

# Convert everything to 升 (1 dou = 10 sheng)
粟總升 = (粟斗 * 10) + 粟升

# 以粟求鑿飯，二十四之二十五而一
鑿飯升 = Fraction(25 * 粟總升, 24)

# Convert back to dou and sheng
鑿飯斗 = 鑿飯升 // 10  # Whole dou
鑿飯剩升 = 鑿飯升 % 10  # Remaining sheng

a = Fraction(鑿飯斗) + Fraction(鑿飯剩升, 10)  # Final result in dou (including fractional part)
"""
Variable 'a' has wrong value. Expected: 1032/125, Actual: 215/24"""
