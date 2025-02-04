"""
又有積七萬一千八百二十四步。問︰為方幾何？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 71,824 cubic bu (步³).
Question: if it is made into a cube, what is the side length of the cube?

Answer: the side length is *a* bu (步).
"""

# 積七萬一千八百二十四步
volume = 71824

# To find the side length of the cube, take the cube root of the volume.
# Since we are not using external libraries, we calculate the cube root manually.

# Initialize variables
a = 0  # side length
while a**3 < volume:
    a += 1

# Check if the cube of `a` matches the volume
if a**3 != volume:
    a -= 1  # Adjust if the cube of `a` exceeds the volume

# The side length of the cube is `a`步
a = Fraction(a)  # Represent as a fraction if needed#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 268, Actual: 41"""
