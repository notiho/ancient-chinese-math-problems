"""
又有積二萬五千二百八十一步。問︰為方幾何？
荅曰： a步 。
"""

"""
Suppose there is a volume of 25,280 cubic bu (步³).
Question: what is the side length of the cube?

Answer: the side length is *a* bu (步).
"""

# 積二萬五千二百八十一步
volume = 25280

# To find the side length of the cube, take the cube root of the volume.
# Since we cannot use external libraries, we will approximate the cube root manually.

# Initialize variables
a = 1  # Start with an initial guess for the cube root

# Use a simple iterative method to approximate the cube root
while a**3 < volume:
    a += 1

# If the cube of `a` exceeds the volume, the actual side length is slightly less
if a**3 > volume:
    a -= 1

# Result
a = Fraction(a)  # Represent the result as a fraction if needed
"""
Variable 'a' has wrong value. Expected: 159, Actual: 29"""
