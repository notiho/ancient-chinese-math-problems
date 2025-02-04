"""
今有稻一十二斗六升、一十五分升之一十四，欲為粟。問︰得幾何？
荅曰：為粟 a斗 。
"""

"""
Suppose there is 12 dou, 6 sheng, and 14/15 of a sheng of rice. It is desired to turn it into unhusked millet.
Question: how much unhusked millet does it make?

Answer: it makes *a* dou of unhusked millet.
"""

from fractions import Fraction

# 稻一十二斗六升、一十五分升之一十四
稻斗 = 12
稻升 = 6 + Fraction(14, 15)

# Convert everything to sheng (1 dou = 10 sheng)
稻總升 = 稻斗 * 10 + 稻升

# Rice to millet conversion: multiply by 2 and divide by 3
粟總升 = Fraction(2 * 稻總升, 3)

# Convert back to dou (1 dou = 10 sheng)
a = Fraction(粟總升, 10)

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 476/45, Actual: 1904/225"""
