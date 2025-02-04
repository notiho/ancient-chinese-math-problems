"""
今有股四尺，弦五尺，問︰為句幾何？
荅曰： a尺 。
"""

"""
Suppose there is a right triangle where the base (gu) is 4 chi and the hypotenuse (xian) is 5 chi.
Question: how long is the height (ju)?

Answer: *a* chi.
"""

# 股 (base) = 4 尺
股 = 4

# 弦 (hypotenuse) = 5 尺
弦 = 5

# Use the Pythagorean theorem: 弦^2 = 股^2 + 句^2
# Solve for 句 (height): 句 = sqrt(弦^2 - 股^2)

a = (弦**2 - 股**2)**0.5  # Calculate the height (句) in chi

a
"""
"""
