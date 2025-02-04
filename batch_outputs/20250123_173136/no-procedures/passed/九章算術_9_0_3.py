"""
今有句三尺，股四尺，問︰為弦幾何？
荅曰： a尺 。
"""

"""
Suppose there is a right triangle with one leg (ju) of 3 chi and the other leg (gu) of 4 chi.
Question: how long is the hypotenuse (xian)?

Answer: the hypotenuse is *a* chi.
"""

# 句 (one leg) = 3 尺
句 = 3

# 股 (other leg) = 4 尺
股 = 4

# Use the Pythagorean theorem to calculate the hypotenuse
# 弦 = sqrt(句^2 + 股^2)
弦_squared = 句**2 + 股**2

# Since we cannot use external functions, we calculate the square root manually
# Find the square root of 弦_squared
a = 0
while a * a < 弦_squared:
    a += Fraction(1, 1000)  # Increment in small steps to approximate the square root

# Final result for the hypotenuse
a
"""
"""
