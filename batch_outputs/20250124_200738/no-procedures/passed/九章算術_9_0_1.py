"""
今有句三尺，股四尺，問︰為弦幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle with one leg (ju) of 3 chi and the other leg (gu) of 4 chi.
Question: how long is the hypotenuse (xian)?

Answer: it is *a* chi.
"""

# 句 (one leg) = 3 尺
句 = 3

# 股 (other leg) = 4 尺
股 = 4

# Using the Pythagorean theorem: 弦 = sqrt(句^2 + 股^2)
弦_squared = 句**2 + 股**2

# 弦 = square root of 弦_squared
# Since the square root of a perfect square is an integer, we can directly calculate it
a = int(弦_squared**0.5)

# Output the result
a#----- content ends here -----

"""
"""
