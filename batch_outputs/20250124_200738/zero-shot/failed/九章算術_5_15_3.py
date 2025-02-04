"""
今有圓亭，下周三丈，上周二丈，高一丈。問︰積幾何？
術曰：上、下周相乘，又各自乘，并之，以高乘之，三十六而一。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a frustum of a circular cone (a truncated cone). The formula provided in the problem is essentially the formula for the volume of a frustum:

\[
V = \frac{\pi h}{3} \left( R_1^2 + R_1 R_2 + R_2^2 \right)
\]

Where:
- \( R_1 \) is the radius of the bottom circle (下周),
- \( R_2 \) is the radius of the top circle (上周),
- \( h \) is the height of the frustum (高),
- \( \pi \) is the mathematical constant (not explicitly mentioned in the problem but implied).

The problem states:
- 下周 (bottom circumference) = 3丈,
- 上周 (top circumference) = 2丈,
- 高 (height) = 1丈.

From the circumference, we can calculate the radius using the formula \( C = 2\pi r \), or \( r = \frac{C}{2\pi} \).

Finally, the volume is divided by 36 to convert the units into 尺 (as per the problem's instructions).

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
bottom_circumference = Fraction(3)  # in 丈
top_circumference = Fraction(2)    # in 丈
height = Fraction(1)               # in 丈

# Convert circumferences to radii
pi = Fraction(355, 113)  # Approximation of π
R1 = bottom_circumference / (2 * pi)  # Radius of the bottom circle in 丈
R2 = top_circumference / (2 * pi)    # Radius of the top circle in 丈

# Calculate the volume of the frustum
volume = (pi * height * (R1**2 + R1 * R2 + R2**2)) / 3  # Volume in 丈³

# Convert volume to 尺³ (1 丈³ = 36 尺³)
a = volume * 36

# The result is stored in variable 'a'
a
#----- content ends here -----


"""


The variable `a` will contain the volume of the frustum in 尺³.
"""


"""
Variable 'a' has wrong value. Expected: 4750/9, Actual: 6441/355"""
