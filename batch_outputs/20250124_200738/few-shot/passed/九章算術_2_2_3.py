"""
今有粟四斗五升，欲為鑿米。問︰得幾何？
術曰：以粟求鑿米，十二之，二十五而一。
荅曰：為鑿米 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 4 dou and 5 sheng of unhusked millet. It is desired to turn it into polished rice.
Question: how much polished rice does one obtain?

The procedure says: when seeking polished rice from unhusked millet, multiply by 12 and divide by 25.

The answer says: it makes *a* dou of polished rice.
"""

# 粟四斗五升
粟斗 = 4
粟升 = 5

# Convert everything to 升 (1 斗 = 10 升)
粟 = 粟斗 * 10 + 粟升

# 以粟求鑿米，十二之
鑿米 = 12 * 粟

# 二十五而一
a = Fraction(鑿米, 25) / 10  # Convert back to dou (1 斗 = 10 升)#----- content ends here -----

"""
"""
