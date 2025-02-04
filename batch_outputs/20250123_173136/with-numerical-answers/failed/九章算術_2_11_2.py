"""
今有粟四斗一升、太半升，欲為答。問︰得幾何？
術曰：以粟求菽、答、麻、麥，皆九之，十而一。
荅曰：為答 a(=15/4)斗 。
"""

"""
Suppose there is 4 dou, 1 sheng, and half a sheng of millet. It is desired to convert it into da (a type of grain).
Question: how much da is obtained?

The procedure says: When seeking beans, da, hemp, or wheat from millet, multiply by 9 and divide by 10.

Answer: it makes *a*(=15/4) dou of da.
"""

from fractions import Fraction

# 粟四斗一升、太半升
粟 = 4 + Fraction(1, 10) + Fraction(1, 20)  # Convert 4 dou, 1 sheng, and half a sheng into dou

# 皆九之
答 = 9 * 粟

# 十而一
a = Fraction(答, 10)  # 15/4 dou
"""
Variable 'a' has wrong value. Expected: 15/4, Actual: 747/200"""
