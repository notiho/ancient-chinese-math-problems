"""
今有丁二萬三千六百九十二人，責兵五千九百二十三人。問：㡬何丁出一兵？
答曰： a 丁出 b 兵。
"""

"""
Suppose there are 23,692 adult males (丁), and 5,923 soldiers are required.
Question: how many adult males are needed to provide one soldier?

Answer: *a* adult males provide *b* soldiers.
"""

# Total adult males
丁 = 23692

# Total soldiers required
兵 = 5923

# Simplify the ratio of 丁 to 兵
from fractions import Fraction

ratio = Fraction(丁, 兵)

# Extract numerator and denominator
a = ratio.numerator
b = ratio.denominator

# The result is: a 丁出 b 兵
a, b
"""
"""
