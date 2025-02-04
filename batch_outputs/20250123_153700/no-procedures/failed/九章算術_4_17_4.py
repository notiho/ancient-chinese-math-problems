"""
今有積三百步。問︰為圓周幾何？
荅曰： a步 。
"""

"""
Suppose there is a circular area of 300 bu².
Question: what is the circumference of the circle?

Answer: the circumference is *a* bu.
"""

# 積三百步
積 = 300

# Formula for the area of a circle: A = (C / 2π)² * π
# Rearranging to find the circumference C: C = 2 * √(A * π)

# Using the ancient Chinese approximation for π as 3
π = 3

# Calculate the radius squared
radius_squared = 積 / π

# Calculate the radius
radius = Fraction(radius_squared).sqrt()

# Calculate the circumference
a = 2 * π * radius
"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
