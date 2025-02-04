"""
今有股四尺，弦五尺，問︰為句幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the "gu" (leg) is 4 chi, and the "xian" (hypotenuse) is 5 chi.
Question: how long is the "ju" (other leg)?

Answer: it is *a* chi.
"""

# 股 (one leg)
股 = 4

# 弦 (hypotenuse)
弦 = 5

# Using the Pythagorean theorem: 弦^2 = 股^2 + 句^2
# Solve for 句 (other leg)
句_squared = 弦**2 - 股**2
a = 句_squared**0.5  # Take the square root to find the length of 句

a#----- content ends here -----

"""
"""
