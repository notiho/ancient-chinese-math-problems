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
import math

# Given area
積 = 1518 + Fraction(3, 4)

# Formula for the area of a circle: A = π * r²
# Solving for radius: r = sqrt(A / π)
radius = math.sqrt(float(積) / math.pi)

# Formula for circumference: C = 2 * π * r
圓周 = 2 * math.pi * radius

# Convert the circumference back to a fraction (approximation)
a = Fraction(圓周).limit_denominator(1000)

a
"""
Variable 'a' has wrong value. Expected: 135, Actual: 69489/503"""
