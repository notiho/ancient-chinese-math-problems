"""
今有方亭，下方五丈，上方四丈，高五丈。問︰積幾何？
術曰：上下方相乘，又各自乘，并之，以高乘之，三而一。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a frustum of a square pyramid. The formula for the volume of a frustum is given by:

\[
V = \frac{h}{3} \times (A_1 + A_2 + \sqrt{A_1 \cdot A_2})
\]

Where:
- \( h \) is the height of the frustum.
- \( A_1 \) is the area of the bottom square.
- \( A_2 \) is the area of the top square.

Given:
- Bottom side = 5 丈 (zhang)
- Top side = 4 丈 (zhang)
- Height = 5 丈 (zhang)

We will compute the volume in terms of cubic 尺 (chi), as 1 丈 = 10 尺. Here's the Python code:


"""


from fractions import Fraction

# Dimensions in 尺
bottom_side = 5 * 10  # 5 丈 = 50 尺
top_side = 4 * 10     # 4 丈 = 40 尺
height = 5 * 10       # 5 丈 = 50 尺

# Areas of the squares
A1 = bottom_side ** 2  # Area of the bottom square
A2 = top_side ** 2     # Area of the top square

# Volume calculation
a = Fraction(height, 3) * (A1 + A2 + Fraction((A1 * A2) ** 0.5))

# The result is stored in variable 'a'
a


"""


The variable `a` will contain the volume of the frustum in cubic 尺.
"""


"""
"""
