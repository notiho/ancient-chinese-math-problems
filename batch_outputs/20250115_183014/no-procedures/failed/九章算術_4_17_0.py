"""
今有積三百步。問︰為圓周幾何？
荅曰： a步 。
"""

"""
Suppose there is an area of 300 bu (square bu) in a circular shape.
Question: what is the circumference of the circle?

Answer: the circumference is *a* bu.
"""

# 積三百步
積 = 300

# Formula for the area of a circle: A = (C / 4)^2 * π, where C is the circumference.
# Rearranging for C: C = 4 * sqrt(A / π)

# Using π = 3 (ancient Chinese approximation)
π = 3

# Solve for circumference
a = 4 * Fraction(積, π).sqrt()  # Using the square root of (A / π)
"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
