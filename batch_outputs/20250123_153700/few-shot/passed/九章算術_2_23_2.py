"""
今有稻一十二斗六升、一十五分升之一十四，欲為粟。問︰得幾何？
術曰：以稻求粟，五之，六而一。
荅曰：為粟 a斗 。
"""

"""
Suppose there is 12 dou, 6 sheng, and 14/15 of a sheng of rice. It is desired to convert it into millet.
Question: how much millet is obtained?

The procedure says: When seeking millet using rice, multiply by 5 and divide by 6.

Answer: it makes *a* dou of millet.
"""

from fractions import Fraction

# 稻一十二斗六升、一十五分升之一十四
稻 = 12  # 12斗
稻 += Fraction(6, 10)  # 6升 (1斗 = 10升)
稻 += Fraction(14, 15 * 10)  # 14/15升 (convert to dou)

# 以稻求粟，五之
粟 = 5 * 稻

# 六而一
a = Fraction(粟, 6)  # Convert to dou

a
"""
"""
