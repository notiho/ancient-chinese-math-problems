"""
今有粟七斗八升，欲為豉。問︰得幾何？
術曰：以粟求豉，六十三之，五十而一。
荅曰：為豉 a(=2457/250)斗 。
"""

"""
Suppose there are 7 dou and 8 sheng of millet. It is desired to turn it into fermented soybeans (chi).
Question: how much does one obtain?

The procedure says: when seeking fermented soybeans (chi) using millet, multiply by 63 and divide by 50.

The answer says: *a*(=2457/250) dou of fermented soybeans.
"""

from fractions import Fraction

# 粟七斗八升
粟斗 = 7
粟升 = 8

# Convert 粟 to 升 (1 斗 = 10 升)
粟 = (粟斗 * 10) + 粟升

# 以粟求豉，六十三之
豉 = 63 * 粟

# 五十而一
a = Fraction(豉, 50) / 10  # Convert back to dou (divide by 10) -> 2457/250 dou
"""
"""
