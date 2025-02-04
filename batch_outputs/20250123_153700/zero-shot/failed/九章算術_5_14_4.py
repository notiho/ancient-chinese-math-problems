"""
今有方亭，下方五丈，上方四丈，高五丈。問︰積幾何？
術曰：上下方相乘，又各自乘，并之，以高乘之，三而一。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a frustum of a square pyramid. The formula for the volume of a frustum is given as:

\[
V = \frac{h}{3} \times (A_1 + A_2 + \sqrt{A_1 \times A_2})
\]

Where:
- \( h \) is the height of the frustum,
- \( A_1 \) is the area of the base (larger square),
- \( A_2 \) is the area of the top (smaller square).

In this problem:
- The side length of the base is 5 丈 (zhang),
- The side length of the top is 4 丈 (zhang),
- The height is 5 丈 (zhang).

We will compute the volume step by step.


"""


from fractions import Fraction

# Given dimensions
side_base = Fraction(5)  # 5 丈
side_top = Fraction(4)   # 4 丈
height = Fraction(5)     # 5 丈

# Calculate areas of the base and top
A1 = side_base ** 2  # Area of the base
A2 = side_top ** 2   # Area of the top

# Calculate the volume using the formula
a = (height / 3) * (A1 + A2 + (A1 * A2) ** Fraction(1, 2))

# The result is in cubic 丈
a


"""


The variable `a` will hold the volume of the frustum in cubic 丈.
"""


"""
Variable 'a' has wrong value. Expected: 305000/3, Actual: 101.66666666666667"""
