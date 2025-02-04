"""
今有粟一十斗八升五分升之二欲為麥問得幾何
術曰以粟求菽答麻麥皆九之十而一
荅曰為麥 a斗 
"""

"""
Suppose there is 10 dou, 8 sheng, and 2/5 of a sheng of millet. It is desired to convert it into wheat.
Question: how much wheat is obtained?

The procedure says: When seeking beans, hemp, or wheat from millet, multiply by 9 and divide by 10.

The answer says: it makes *a* dou of wheat.
"""

from fractions import Fraction

# 粟一十斗八升五分升之二
粟斗 = 10
粟升 = 8 + Fraction(2, 5)  # Convert the fractional part into a Fraction object

# Convert everything to sheng (1 dou = 10 sheng)
粟總升 = 粟斗 * 10 + 粟升

# 以粟求麥，九之十而一
麥總升 = Fraction(9, 10) * 粟總升

# Convert back to dou and sheng
麥斗 = 麥總升 // 10  # Integer part is the number of dou
麥升 = 麥總升 % 10  # Remainder is the number of sheng

a = 麥斗 + 麥升 / 10  # Final answer in dou (including fractional part)
"""
"""
