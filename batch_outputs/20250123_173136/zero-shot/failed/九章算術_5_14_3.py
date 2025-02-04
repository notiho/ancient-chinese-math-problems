"""
今有方亭，下方五丈，上方四丈，高五丈。問︰積幾何？
術曰：上下方相乘，又各自乘，并之，以高乘之，三而一。
荅曰： a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem describes a frustum of a square pyramid (a truncated square pyramid) with the following dimensions:

- Bottom side length: 5 丈 (zhang)
- Top side length: 4 丈 (zhang)
- Height: 5 丈 (zhang)

The formula provided in the problem is essentially the volume formula for a frustum of a square pyramid:

\[
V = \frac{h}{3} \times (A_1 + A_2 + \sqrt{A_1 \cdot A_2})
\]

Where:
- \( h \) is the height of the frustum,
- \( A_1 \) is the area of the bottom square,
- \( A_2 \) is the area of the top square.

Now, let's compute the volume in Python:


"""


from fractions import Fraction

# Dimensions in zhang
bottom_side = Fraction(5)  # Bottom side length in zhang
top_side = Fraction(4)     # Top side length in zhang
height = Fraction(5)       # Height in zhang

# Areas of the bottom and top squares
A1 = bottom_side ** 2  # Area of the bottom square
A2 = top_side ** 2     # Area of the top square

# Volume formula for a frustum of a square pyramid
a = (height / 3) * (A1 + A2 + (A1 * A2) ** Fraction(1, 2))  # Volume in cubic zhang

# The result is stored in the variable 'a'
a


"""


The variable `a` will contain the volume of the frustum in cubic 丈 (zhang³).
"""


"""
Variable 'a' has wrong value. Expected: 305000/3, Actual: 101.66666666666667"""
