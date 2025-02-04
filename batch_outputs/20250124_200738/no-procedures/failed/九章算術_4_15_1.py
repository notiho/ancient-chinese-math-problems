"""
又有積三十九億七千二百一十五萬六百二十五步。問︰為方幾何？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 3,972,156,625 cubic bu (步³).
Question: what is the side length of the cube (in bu)?

Answer: the side length is *a* bu.
"""

# Given volume in cubic bu
volume = 3972156625

# To find the side length of the cube, we take the cube root of the volume.
# Since we cannot use external libraries, we will calculate the cube root manually using integer approximation.

# Start with an initial guess
a = 1

# Incrementally find the cube root
while a**3 < volume:
    a += 1

# Check if the cube of the current value exceeds the volume
if a**3 > volume:
    a -= 1  # Adjust to the correct value

# The side length of the cube is `a` bu
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 63025, Actual: 1583"""
