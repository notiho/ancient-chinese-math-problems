"""
今有粟三斗六升，欲為粺飯。問︰得幾何？
術曰：以粟求粺飯，二十七之，二十五而一。
荅曰：為粺飯 a斗 。
"""

#----- content starts here -----
"""
Suppose there is 3 dou and 6 sheng of millet. It is desired to turn it into polished rice.
Question: how much polished rice does one obtain?

The procedure says: when seeking polished rice from millet, multiply by 27 and divide by 25.

The answer says: it makes *a* dou of polished rice.
"""

# 粟三斗六升
粟 = 3 * 10 + 6  # Convert to sheng (1 dou = 10 sheng)

# 以粟求粺飯，二十七之
粺飯 = 27 * 粟

# 二十五而一
粺飯 = Fraction(粺飯, 25)

# Convert back to dou and sheng
a斗 = 粺飯 // 10  # Whole dou
a升 = 粺飯 % 10  # Remaining sheng

a = f"{a斗}斗 {a升}升"#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 486/125, Actual: 3斗 222/25升"""
