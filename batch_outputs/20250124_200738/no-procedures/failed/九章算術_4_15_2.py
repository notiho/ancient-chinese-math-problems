"""
又有積三十九億七千二百一十五萬六百二十五步。問︰為方幾何？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 3,972,156,625 cubic bu (步³).
Question: what is the side length of a cube (in bu) with this volume?

Answer: the side length is *a* bu.
"""

# Given volume in cubic bu
volume = 3972156625

# To find the side length of the cube, take the cube root of the volume
# We will solve this manually using integer approximation since Python does not have a built-in cube root function.

# Start with an initial guess for the cube root
a = 1
while a**3 <= volume:
    a += 1

# The correct side length is one less than the overshot value
a -= 1

# Final result
a = Fraction(a)  # Represent the result as a fraction if needed#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 63025, Actual: 1583"""
