"""
今有粟三斗六升欲為粺飯問得幾何
術曰以粟求粺飯二十七之二十五而一
荅曰為粺飯 a斗 
"""

#----- content starts here -----
"""
Suppose there are 3 dou and 6 sheng of millet. It is desired to turn it into polished rice.
Question: how much polished rice does one obtain?

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
粺飯 = Fraction(粺飯, 25)

# Convert back to 斗 (1 斗 = 10 升)
a斗 =粺飯 // 10
a升 =粺飯 % 10
a=f"{a斗}斗{a升}"#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 486/125, Actual: 3斗222/25"""
