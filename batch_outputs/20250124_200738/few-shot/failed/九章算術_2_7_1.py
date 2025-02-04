"""
今有粟三斗六升，欲為粺飯。問︰得幾何？
術曰：以粟求粺飯，二十七之，二十五而一。
荅曰：為粺飯 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 3 dou and 6 sheng of millet. It is desired to turn it into polished rice.
Question: how much polished rice does it make?

The procedure says: When seeking polished rice from millet, multiply by 27 and divide by 25.

The answer says: it makes *a* dou of polished rice.
"""

# 粟三斗六升
粟斗 = 3
粟升 = 6

# Convert everything to 升 (1 斗 = 10 升)
粟 = 粟斗 * 10 + 粟升

# 以粟求粺飯，二十七之
粺飯 = 27 * 粟

# 二十五而一
a = Fraction(粺飯, 25)

# Convert result back to 斗 and 升
粺飯斗 = a // 10  # Whole number of 斗
粺飯升 = a % 10   # Remaining 升

粺飯斗, 粺飯升#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 486/125, Actual: 972/25"""
