"""
今有粟七斗九升欲為御米問得幾何
術曰以粟求御米二十一之五十而一
荅曰為御米 a斗 
"""

#----- content starts here -----
"""
Suppose there are 7 dou and 9 sheng of millet. It is desired to turn it into polished rice.
Question: how much polished rice does one obtain?

The procedure says: when seeking polished rice from millet, multiply by 21 and divide by 50.

The answer says: it makes *a* dou of polished rice.
"""

# 粟七斗九升
粟斗 = 7
粟升 = 9

# Convert to 升 (1 斗 = 10 升)
粟 = (粟斗 * 10) + 粟升

# 以粟求御米，二十一之
御米 = 21 * 粟

# 五十而一
御米 = Fraction(御米, 50)

# Convert back to 斗 (1 斗 = 10 升)
a = Fraction(御米, 10)  # Result in dou#----- content ends here -----

"""
"""
