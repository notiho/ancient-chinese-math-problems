"""
今有股四尺，弦五尺，問︰為句幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the "gu" (one leg) is 4 chi and the hypotenuse (xian) is 5 chi.
Question: how long is the other leg, "ju"?

Answer: *a* chi.
"""

# 股 (one leg) = 4 尺
股 = 4

# 弦 (hypotenuse) = 5 尺
弦 = 5

# Using the Pythagorean theorem: 弦^2 = 股^2 + 句^2
# Solve for 句 (the other leg)
句_squared = 弦**2 - 股**2
句 = Fraction(句_squared).sqrt()

# Answer
a = 句#----- content ends here -----

"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
