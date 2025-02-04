"""
今有粟二斗一升欲為粺米問得幾何
術曰以粟求粺米二十七之五十而一
荅曰為粺米 a斗 
"""

"""
Suppose there are 2 dou and 1 sheng of unhusked millet. It is desired to turn it into polished millet.
Question: how much polished millet does one obtain?

The procedure says: when seeking polished millet using unhusked millet, multiply by 27 and divide by 50.

The answer says: it makes *a* dou of polished millet.
"""

# 粟二斗一升
粟斗 = 2
粟升 = 1

# Convert everything to 升 (1 dou = 10 sheng)
粟總升 = (粟斗 * 10) + 粟升

# 以粟求粺米，二十七之
粺米 = 27 * 粟總升

# 五十而一
粺米 = Fraction(粺米, 50)

# Convert back to dou (1 dou = 10 sheng)
a = Fraction(粺米, 10)  # Result in dou
"""
"""
