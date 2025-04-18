"""
今有粟四斗一升、太半升，欲為答。問︰得幾何？
術曰：以粟求菽、答、麻、麥，皆九之，十而一。
荅曰：為答 a斗 。
"""

"""
Suppose there is 4 dou, 1 sheng, and half a sheng of millet. It is desired to convert it into da (a type of grain).
Question: how much da is obtained?

The procedure says: When seeking shu (beans), da, ma (hemp), or mai (wheat) from millet, multiply by 9 and divide by 10.

The answer says: it makes *a* dou of da.
"""

from fractions import Fraction

# 粟四斗一升、太半升
粟 = 4 * 10 + 1 + Fraction(1, 2)  # Convert everything to sheng (1 dou = 10 sheng)

# 皆九之
答 = 9 * 粟

# 十而一
答 = Fraction(答, 10)

# Convert back to dou and sheng
a斗 = 答 // 10  # Whole dou
a升 = 答 % 10   # Remaining sheng

a = f"{a斗}斗 {a升}升"

"""
Variable 'a' has wrong value. Expected: 15/4, Actual: 3斗 147/20升"""
