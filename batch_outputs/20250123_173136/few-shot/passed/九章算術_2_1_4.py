"""
今有粟二斗一升，欲為粺米。問︰得幾何？
術曰：以粟求粺米，二十七之，五十而一。
荅曰：為粺米 a斗 。
"""

"""
Suppose there are 2 dou and 1 sheng of unhusked millet. It is desired to turn it into polished millet.
Question: how much polished millet does one obtain?

The procedure says: when seeking polished millet from unhusked millet, multiply by 27 and divide by 50.

The answer says: it makes *a* dou of polished millet.
"""

# 粟二斗一升
粟 = 2 * 10 + 1  # Convert to sheng (1 dou = 10 sheng)

# 以粟求粺米，二十七之
粺米 = 27 * 粟

# 五十而一
粺米 = Fraction(粺米, 50)

# Convert back to dou and sheng
a斗 = 粺米 // 10  # Whole dou
a升 = 粺米 % 10  # Remaining sheng

a = Fraction(a斗) + Fraction(a升, 10)  # Final result in dou
"""
"""
