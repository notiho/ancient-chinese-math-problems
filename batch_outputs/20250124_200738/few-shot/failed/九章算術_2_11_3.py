"""
今有粟四斗一升、太半升，欲為答。問︰得幾何？
術曰：以粟求菽、答、麻、麥，皆九之，十而一。
荅曰：為答 a斗 。
"""

#----- content starts here -----
"""
Suppose there is 4 dou, 1 sheng, and half a sheng of millet. It is desired to convert it into da (a type of grain).
Question: how much da is obtained?

The procedure says: When seeking shu (beans), da, ma (hemp), or mai (wheat) from millet, multiply by 9 and divide by 10.

The answer says: it makes *a* dou of da.
"""

from fractions import Fraction

# 粟四斗一升、太半升
粟 = 4 * 10 + 1 + Fraction(1, 2)  # Convert to sheng (1 dou = 10 sheng)

# 以粟求答，皆九之
答 = 9 * 粟

# 十而一
a = Fraction(答, 10)  # Result in sheng

# Convert result to dou and sheng
a斗 = a // 10  # Whole dou
a升 = a % 10  # Remaining sheng

a = (a斗, a升)  # Final result in dou and sheng#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 15/4, Actual: (3, Fraction(147, 20))"""
