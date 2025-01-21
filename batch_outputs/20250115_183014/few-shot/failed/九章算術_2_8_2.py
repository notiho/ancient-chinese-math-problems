"""
今有粟八斗六升，欲為鑿飯。問︰得幾何？
術曰：以粟求鑿飯，二十四之，二十五而一。
荅曰：為鑿飯 a斗 。
"""

"""
Suppose there are 8 dou and 6 sheng of millet. It is desired to turn it into cooked rice.
Question: how much cooked rice does it make?

The procedure says: when seeking cooked rice from millet, multiply by 24 and divide by 25.

The answer says: it makes *a* dou of cooked rice.
"""

# 粟八斗六升
粟斗 = 8
粟升 = 6

# Convert everything to 升 (1 斗 = 10 升)
粟 = 10 * 粟斗 + 粟升

# 以粟求鑿飯，二十四之
鑿飯 = 24 * 粟

# 二十五而一
a = Fraction(鑿飯, 25)

# Convert back to 斗 if needed
a斗 = a // 10  # Whole dou
a升 = a % 10   # Remaining sheng

a = (a斗, a升)  # Representing the result as (斗, 升)
"""
Variable 'a' has wrong value. Expected: 1032/125, Actual: (8, Fraction(64, 25))"""
