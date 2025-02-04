"""
今有股四尺，弦五尺，問︰為句幾何？
荅曰： a尺 。
"""

"""
Suppose there is a right triangle with a leg (gu) of 4 chi and a hypotenuse (xian) of 5 chi.
Question: how long is the other leg (ju)?

Answer: it is *a* chi.
"""

# 股 (one leg of the triangle)
股 = 4

# 弦 (hypotenuse of the triangle)
弦 = 5

# Using the Pythagorean theorem: 弦^2 = 股^2 + 句^2
# Solve for 句 (the other leg)
句_squared = 弦**2 - 股**2
句 = Fraction(句_squared).sqrt()

# Answer
a = 句
"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
