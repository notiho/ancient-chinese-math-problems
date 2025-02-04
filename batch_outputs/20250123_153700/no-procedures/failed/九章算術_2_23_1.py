"""
今有稻一十二斗六升、一十五分升之一十四，欲為粟。問︰得幾何？
荅曰：為粟 a斗 。
"""

"""
Suppose there is 12 dou, 6 sheng, and 14/15 of a sheng of rice. It is desired to turn it into millet.
Question: how much millet does it make?

Answer: it makes *a* dou of millet.
"""

from fractions import Fraction

# 稻一十二斗六升、一十五分升之一十四
稻 = 12 + Fraction(6, 10) + Fraction(14, 15 * 10)

# Conversion ratio: rice to millet is 2/3
a = 稻 * Fraction(2, 3)

# Result
a
"""
Variable 'a' has wrong value. Expected: 476/45, Actual: 1904/225"""
