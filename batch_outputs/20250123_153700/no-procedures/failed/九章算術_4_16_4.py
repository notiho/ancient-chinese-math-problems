"""
今有積一千五百一十八步、四分步之三。問︰為圓周幾何？
荅曰： a步 。
"""

"""
Suppose there is an area of 1518 and 3/4 bu² (square bu). 
Question: what is the circumference of the circle?

Answer: the circumference is *a* bu.
"""

from fractions import Fraction

# Given area
積 = 1518 + Fraction(3, 4)

# Formula for the area of a circle: A = (C^2) / (4 * π)
# Rearranging for circumference (C): C = sqrt(A * 4 * π)
# Using an approximation for π = 3 (as was common in ancient Chinese mathematics)

π = 3

# Calculate the circumference
a = Fraction(4 * 積 * π).sqrt()

# Output the result
a
"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
