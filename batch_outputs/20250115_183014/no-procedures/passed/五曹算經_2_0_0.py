"""
今有丁二萬三千六百九十二人，責兵五千九百二十三人。問：㡬何丁出一兵？
答曰： a 丁出 b 兵。
"""

"""
Suppose there are 23,692 adult males (丁), and 5,923 soldiers are required.
Question: how many adult males are needed to provide one soldier?

Answer: *a* adult males provide *b* soldiers.
"""

# 丁總數
total_ding = 23692

# 兵總數
total_bing = 5923

# Calculate how many 丁 are needed to provide 1 兵
a = total_ding
b = total_bing

# Simplify the ratio
from fractions import Fraction
ratio = Fraction(a, b)
a = ratio.numerator
b = ratio.denominator

# Result: a 丁出 b 兵
"""
"""
