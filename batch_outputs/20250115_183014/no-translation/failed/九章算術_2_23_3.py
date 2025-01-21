"""
今有稻一十二斗六升、一十五分升之一十四，欲為粟。問︰得幾何？
術曰：以稻求粟，五之，六而一。
荅曰：為粟 a斗 。
"""

"""

"""


from fractions import Fraction

# 稻一十二斗六升、一十五分升之一十四
稻 = 12 + Fraction(6, 10) + Fraction(1, 15 * 14)

# 以稻求粟，五之
粟 = 5 * 稻

# 六而一
a = Fraction(粟, 6)


"""

"""


"""
Variable 'a' has wrong value. Expected: 476/45, Actual: 2647/252"""
