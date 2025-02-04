"""
又有積三十九億七千二百一十五萬六百二十五步。問︰為方幾何？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 3,972,156,625 cubic bu (步³).
Question: if this volume is a cube, what is the length of one side?

The answer says: *a* bu.
"""

# Total volume in cubic bu
volume = 3972156625

# To find the side length of the cube, we need the cube root of the volume.
# Since we cannot use external libraries, we will calculate it manually using an iterative method.

# Start with an initial guess for the cube root
a = 1

# Use a simple iterative method to approximate the cube root
for _ in range(100):  # Perform 100 iterations for better precision
    a = (2 * a + volume / (a * a)) // 3  # Newton's method for cube root

# The result is the side length of the cube in bu
a = int(a)  # Convert to an integer since the problem assumes whole bu units#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 63025, Actual: 1583"""
