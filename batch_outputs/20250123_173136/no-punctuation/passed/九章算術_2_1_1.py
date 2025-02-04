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
粟 = 2 * 10 + 1  # Convert to sheng (1 dou = 10 sheng)

# 以粟求粺米，二十七之
粺米 = 27 * 粟

# 五十而一
粺米 = Fraction(粺米, 50)

# Convert back to dou
a = Fraction(粺米, 10)  # Convert sheng to dou (1 dou = 10 sheng)
"""
"""
