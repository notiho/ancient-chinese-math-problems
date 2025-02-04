"""
今有積，二十三萬四千五百六十七步。問：為方幾何？
答曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 234,567 cubic bu (步³).
Question: what is the side length of the cube (in bu)?

Answer: the side length is *a* bu.
"""

# Import Fraction for precise calculations
from fractions import Fraction

# Given volume
volume = 234567

# To find the side length of the cube, we need the cube root of the volume.
# Since we cannot use external libraries, we will approximate the cube root manually.

# Start with an initial guess for the cube root
side_length = 60  # Initial guess (since 60³ = 216,000, close to 234,567)

# Refine the guess using a simple iterative method
for _ in range(10):  # Perform 10 iterations for better accuracy
    side_length = Fraction(2 * side_length + Fraction(volume, side_length**2), 3)

# The final side length
a = side_length

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 468823/968, Actual: Too large to be printed"""
