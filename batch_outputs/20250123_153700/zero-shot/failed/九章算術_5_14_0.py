"""
今有方亭，下方五丈，上方四丈，高五丈。問︰積幾何？
術曰：上下方相乘，又各自乘，并之，以高乘之，三而一。
荅曰： a尺 。
"""

"""
To solve this problem, we will calculate the volume of a frustum of a square pyramid (方亭). The formula provided in the problem is essentially the volume formula for a frustum:

\[
V = \frac{h}{3} \times (A_1 + A_2 + \sqrt{A_1 \times A_2})
\]

Where:
- \( h \) is the height of the frustum,
- \( A_1 \) is the area of the bottom square,
- \( A_2 \) is the area of the top square.

### Given:
- Bottom side length = 5 丈 (so \( A_1 = 5 \times 5 = 25 \) square 丈),
- Top side length = 4 丈 (so \( A_2 = 4 \times 4 = 16 \) square 丈),
- Height = 5 丈.

We will compute the volume in cubic 丈 and convert it to cubic 尺 (1 丈 = 10 尺, so \( 1 \text{ cubic 丈} = 1000 \text{ cubic 尺} \)).

Here is the Python code:


"""


from fractions import Fraction

# Given dimensions
bottom_side = Fraction(5)  # 丈
top_side = Fraction(4)     # 丈
height = Fraction(5)       # 丈

# Calculate areas of the bottom and top squares
A1 = bottom_side ** 2  # Bottom area in square 丈
A2 = top_side ** 2     # Top area in square 丈

# Volume formula for a frustum
volume_in_cubic_zhang = (height / 3) * (A1 + A2 + (A1 * A2) ** Fraction(1, 2))

# Convert volume to cubic 尺
a = volume_in_cubic_zhang * 1000  # 1 cubic 丈 = 1000 cubic 尺

# Result
a  # Volume in cubic 尺


"""


### Final Answer:
The variable `a` will contain the volume of the frustum in cubic 尺.
"""


"""
Variable 'a' has wrong value. Expected: 305000/3, Actual: 101666.66666666667"""
