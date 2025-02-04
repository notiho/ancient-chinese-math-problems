"""
今有積三百步。問︰為圓周幾何？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is an area of 300 bu². It is a circular field.
Question: what is the circumference of the circle?

Answer: the circumference is *a* bu.
"""

# 積三百步
積 = 300

# Formula for the area of a circle: A = (C / 4)^2 * π, where C is the circumference.
# Rearranging for C: C = 2 * sqrt(A * π)

# Using π = 3 (ancient Chinese approximation)
π = 3

# Solve for the circumference
a = Fraction(2 * (積 * π) ** 0.5)  # Circumference in bu#----- content ends here -----

"""
"""
