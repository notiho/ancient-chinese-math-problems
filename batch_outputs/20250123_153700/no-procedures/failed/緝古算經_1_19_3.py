"""
假令有股十六二分之一，句弦相乘冪一百六十四二十五分之十四。問：句多少？
答曰：句 a 。
"""

"""
Suppose there is a right triangle where the leg (股) is 16 1/2 (16.5), and the product of the other leg (句) and the hypotenuse (弦) is 164 14/25 (164.56).
Question: what is the length of the other leg (句)?

Answer: the other leg (句) is *a*.
"""

from fractions import Fraction

# 股 (one leg of the triangle)
股 = Fraction(33, 2)  # 16 1/2

# 冪 (product of 句 and 弦)
冪 = Fraction(4104, 25)  # 164 14/25

# Using the formula: 冪 = 股 * 句
# Solve for 句: 句 = 冪 / 股
句 = 冪 / 股

# Answer
a = 句
a
"""
Variable 'a' has wrong value. Expected: 44/5, Actual: 2736/275"""
