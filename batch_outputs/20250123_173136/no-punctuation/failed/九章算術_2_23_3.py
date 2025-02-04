"""
今有稻一十二斗六升一十五分升之一十四欲為粟問得幾何
術曰以稻求粟五之六而一
荅曰為粟 a斗 
"""

"""
Suppose there is 12 dou, 6 sheng, and 1/14 of a sheng of rice. It is desired to convert it into millet.
Question: how much millet does it make?

The procedure says: when seeking millet from rice, multiply by 5 and divide by 6.

The answer says: it makes *a* dou of millet.
"""

from fractions import Fraction

# 稻一十二斗六升一十五分升之一十四
稻 = 12 + Fraction(6, 10) + Fraction(1, 14 * 10)

# 以稻求粟，五之
粟 = 5 * 稻

# 六而一
a = Fraction(粟, 6)  # Result in dou
"""
Variable 'a' has wrong value. Expected: 476/45, Actual: 1765/168"""
