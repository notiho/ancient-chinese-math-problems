"""
又有積二萬五千二百八十一步。問︰為方幾何？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 25,281 cubic bu (步).
Question: if this volume forms a cube, what is the side length of the cube?

Answer: the side length is *a* bu.
"""

# 積二萬五千二百八十一步
volume = 25281

# To find the side length of the cube, we need the cube root of the volume.
# Since we cannot use external libraries, we will approximate the cube root manually.

# Start with an initial guess
a = 1

# Use a simple iterative method to approximate the cube root
while a**3 < volume:
    a += 1

# If the cube of 'a' exceeds the volume, reduce by 1 to find the correct side length
if a**3 > volume:
    a -= 1

# The result is the side length of the cube
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 159, Actual: 29"""
