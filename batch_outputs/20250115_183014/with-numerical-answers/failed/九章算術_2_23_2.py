"""
今有稻一十二斗六升、一十五分升之一十四，欲為粟。問︰得幾何？
術曰：以稻求粟，五之，六而一。
荅曰：為粟 a(=476/45)斗 。
"""

"""
Suppose there is 12 dou, 6 sheng, and 1/14 of 15 sheng of rice. It is desired to convert it into millet.
Question: how much millet does it make?

The procedure says: when seeking millet using rice, multiply by 5 and divide by 6.

Answer: it makes *a*(=476/45) dou of millet.
"""

from fractions import Fraction

# 稻一十二斗六升、一十五分升之一十四
稻斗 = 12
稻升 = 6
稻分升 = Fraction(1, 14)

# Convert everything to dou (1 dou = 10 sheng, 1 sheng = 1/10 dou)
稻 = 稻斗 + Fraction(稻升, 10) + Fraction(稻分升, 10 * 15)

# 以稻求粟，五之
粟 = 5 * 稻

# 六而一
a = Fraction(粟, 6) # 476/45 dou
"""
Variable 'a' has wrong value. Expected: 476/45, Actual: 26461/2520"""
