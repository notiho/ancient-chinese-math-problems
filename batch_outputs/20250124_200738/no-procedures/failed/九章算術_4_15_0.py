"""
又有積三十九億七千二百一十五萬六百二十五步。問︰為方幾何？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 3,972,156,625 cubic bu (步³).
Question: what is the side length of a cube with this volume?

Answer: the side length is *a* bu (步).
"""

# Given volume in cubic bu
volume = 3972156625

# To find the side length of a cube, take the cube root of the volume.
# Since we cannot use external libraries, we will approximate the cube root manually.

# Start with an initial guess for the cube root
a = 1

# Use a simple iterative method to approximate the cube root
while a**3 < volume:
    a += 1

# If the cube of the current value exceeds the volume, subtract 1 to get the correct value
if a**3 > volume:
    a -= 1

# The side length of the cube is approximately `a` bu
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 63025, Actual: 1583"""
