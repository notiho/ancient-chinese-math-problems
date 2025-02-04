"""
假令有股十六二分之一，句弦相乘冪一百六十四二十五分之十四。問：句多少？
答曰：句 a 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the leg (gu) is 16 1/2 (16.5), and the product of the other leg (ju) and the hypotenuse (xian) is 164 14/25 (164.56).
Question: what is the length of the other leg (ju)?

Answer: the other leg (ju) is *a*.
"""

from fractions import Fraction

# 股 (gu) = 16 1/2
股 = Fraction(33, 2)

# 句弦相乘冪 = 164 14/25
句弦相乘冪 = Fraction(164 * 25 + 14, 25)

# 句 (ju) = 冪 / 股
a = 句弦相乘冪 / 股

# Result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 44/5, Actual: 748/75"""
