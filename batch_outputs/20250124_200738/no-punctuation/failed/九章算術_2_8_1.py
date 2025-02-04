"""
今有粟八斗六升欲為鑿飯問得幾何
術曰以粟求鑿飯二十四之二十五而一
荅曰為鑿飯 a斗 
"""

#----- content starts here -----
"""
Suppose there are 8 dou and 6 sheng of millet. It is desired to turn it into cooked rice.
Question: how much cooked rice does it make?

The procedure says: when seeking cooked rice from millet, multiply by 24 and divide by 25.

The answer says: it makes *a* dou of cooked rice.
"""

# 粟八斗六升
粟斗 = 8
粟升 = 6

# Convert to 升 (1 dou = 10 sheng)
粟 = (粟斗 * 10) + 粟升

# 以粟求鑿飯，二十四之
鑿飯 = 24 * 粟

# 二十五而一
a = Fraction(鑿飯, 25)

# Convert back to dou and sheng
a斗 = a // 10  # Whole dou
a升 = a % 10   # Remaining sheng

a斗, a升  # Final result in dou and sheng#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1032/125, Actual: 2064/25"""
