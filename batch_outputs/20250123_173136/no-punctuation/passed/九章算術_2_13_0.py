"""
今有粟一十斗八升五分升之二欲為麥問得幾何
術曰以粟求菽答麻麥皆九之十而一
荅曰為麥 a斗 
"""

"""
Suppose there is 10 dou, 8 sheng, and 2/5 of a sheng of millet. It is desired to convert it into wheat.
Question: how much wheat does one obtain?

The procedure says: When seeking beans, hemp, or wheat from millet, multiply by 9 and divide by 10.

The answer says: it makes *a* dou of wheat.
"""

from fractions import Fraction

# 粟一十斗八升五分升之二
粟 = 10 + Fraction(8, 10) + Fraction(2, 10 * 5)

# 以粟求麥，九之
麥 = 9 * 粟

# 十而一
a = Fraction(麥, 10)
"""
"""
