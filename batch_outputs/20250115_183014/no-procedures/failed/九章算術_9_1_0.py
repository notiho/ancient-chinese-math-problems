"""
今有弦五尺，句三尺，問︰為股幾何？
荅曰： a尺 。
"""

"""
Suppose there is a right triangle with a hypotenuse (弦) of 5 chi and one leg (句) of 3 chi.
Question: how long is the other leg (股)?

Answer: it is *a* chi.
"""

# 弦 (hypotenuse)
弦 = 5

# 句 (one leg)
句 = 3

# 股 (other leg) is calculated using the Pythagorean theorem: 弦^2 = 句^2 + 股^2
# 股^2 = 弦^2 - 句^2
股_squared = 弦**2 - 句**2

# 股 = square root of 股_squared
# Since we are working with exact values, we use Fraction to represent the square root
a = Fraction(股_squared).sqrt()

# Answer
a
"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
