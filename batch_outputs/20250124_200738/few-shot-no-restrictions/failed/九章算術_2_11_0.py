"""
今有粟四斗一升、太半升，欲為答。問︰得幾何？
術曰：以粟求菽、答、麻、麥，皆九之，十而一。
荅曰：為答 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 4 dou, 1 sheng, and half a sheng of millet. It is desired to convert it into da (a type of grain).
Question: how much da is obtained?

The procedure says: When seeking shu (beans), da, ma (hemp), or mai (wheat) from millet, multiply by 9 and divide by 10.

Answer: it makes *a* dou of da.
"""

from fractions import Fraction

# 粟四斗一升、太半升
粟 = 4  # 4 dou
粟 += 1 / 10  # 1 sheng (1/10 of a dou)
粟 += Fraction(1, 20)  # 太半升 (half a sheng, 1/20 of a dou)

# 以粟求答，九之，十而一
答 = Fraction(9 * 粟, 10)

# Convert result to dou
a = 答
#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
