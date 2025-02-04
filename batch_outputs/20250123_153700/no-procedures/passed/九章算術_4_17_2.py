"""
今有積三百步。問︰為圓周幾何？
荅曰： a步 。
"""

"""
Suppose there is an area of 300 bu² (a square measurement).  
Question: what is the circumference of the circle with this area?

Answer: the circumference is *a* bu.
"""

# 積三百步
積 = 300

# The formula for the area of a circle is A = (C / 4)^2 * π, where C is the circumference.
# Rearranging for C, we get C = 2 * sqrt(A * π).

# Using π = 3 for ancient Chinese calculations:
π = 3

# Solve for the circumference:
a = 2 * Fraction((積 * π) ** (1/2))
"""
"""
