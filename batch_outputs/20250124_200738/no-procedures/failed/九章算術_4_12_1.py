"""
又有積二萬五千二百八十一步。問︰為方幾何？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 25,281 cubic bu (步). 
Question: if it forms a cube, what is the side length of the cube?

Answer: the side length is *a* bu.
"""

# 積二萬五千二百八十一步
volume = 25281

# To find the side length of the cube, we take the cube root of the volume.
# Since we cannot use external libraries, we will approximate the cube root manually.

# Start with an initial guess for the cube root
a = 30  # Initial guess

# Refine the guess using a simple iterative method
while a**3 != volume:
    if a**3 < volume:
        a += 1
    else:
        a -= 1

# The result is the side length of the cube in bu
a = Fraction(a)  # Represent as a fraction if necessary#----- content ends here -----

"""
Timed out"""
