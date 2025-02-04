"""
今有粟三斗少半升欲為菽問得幾何
術曰以粟求菽答麻麥皆九之十而一
荅曰為菽 a斗 
"""

"""
Suppose there is 3 dou and half a sheng of millet. It is desired to turn it into beans.
Question: how much does one obtain?

The procedure says: when seeking beans from millet (and similarly for hemp or wheat), multiply by 9 and divide by 10.

The answer says: it makes *a* dou of beans.
"""

from fractions import Fraction

# 粟三斗少半升
粟 = 3 + Fraction(1, 20)  # Convert 3 dou and half a sheng to dou (1 dou = 10 sheng)

# 以粟求菽，九之
菽 = 9 * 粟

# 十而一
a = Fraction(菽, 10)  # Result in dou
"""
Variable 'a' has wrong value. Expected: 273/100, Actual: 549/200"""
