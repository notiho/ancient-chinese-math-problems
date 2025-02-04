"""
今有鑿米三斗、少半升，欲為粟。問︰得幾何？
荅曰：為粟 a斗 。
"""

"""
Suppose there is 3 dou and half a sheng of polished rice. It is desired to turn it back into unhusked millet.
Question: how much unhusked millet does it make?

Answer: it makes *a* dou of unhusked millet.
"""

from fractions import Fraction

# 鑿米三斗、少半升
鑿米 = 3 + Fraction(1, 2) / 10  # Convert 3 dou and half a sheng into dou

# To convert polished rice back to unhusked millet, multiply by 2 and divide by 3
a = Fraction(2 * 鑿米, 3)

a  # Result in dou
"""
Variable 'a' has wrong value. Expected: 455/72, Actual: 61/30"""
