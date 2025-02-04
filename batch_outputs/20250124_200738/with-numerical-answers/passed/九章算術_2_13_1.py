"""
今有粟一十斗八升、五分升之二，欲為麥。問︰得幾何？
術曰：以粟求菽、答、麻、麥，皆九之，十而一。
荅曰：為麥 a(=2439/250)斗 。
"""

#----- content starts here -----
"""
Suppose there are 10 dou, 8 sheng, and 2/5 of a sheng of millet. It is desired to convert it into wheat.
Question: how much wheat is obtained?

The procedure says: When seeking beans, rice, hemp, or wheat from millet, multiply by 9 and divide by 10.

Answer: it makes *a*(=2439/250) dou of wheat.
"""

from fractions import Fraction

# 粟一十斗八升、五分升之二
粟斗 = 10
粟升 = 8 + Fraction(2, 5)  # Convert the fractional part of sheng

# Convert everything to dou (1 dou = 10 sheng)
粟 = 粟斗 + Fraction(粟升, 10)

# 以粟求麥，皆九之
麥 = 9 * 粟

# 十而一
a = Fraction(麥, 10)  # 2439/250 dou#----- content ends here -----

"""
"""
