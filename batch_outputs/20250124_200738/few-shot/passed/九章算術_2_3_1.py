"""
今有粟七斗九升，欲為御米。問︰得幾何？
術曰：以粟求御米，二十一之，五十而一。
荅曰：為御米 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 7 dou and 9 sheng of millet. It is desired to turn it into polished rice.
Question: how much polished rice does it make?

The procedure says: when seeking polished rice using millet, multiply by 21 and divide by 50.

The answer says: it makes *a* dou of polished rice.
"""

# 粟七斗九升
粟斗 = 7
粟升 = 9

# Convert 粟 to 升 (1 dou = 10 sheng)
粟 = 10 * 粟斗 + 粟升

# 以粟求御米，二十一之
御米 = 21 * 粟

# 五十而一
御米 = Fraction(御米, 50)

# Convert 御米 back to dou (1 dou = 10 sheng)
a = Fraction(御米, 10)  # Result in dou#----- content ends here -----

"""
"""
