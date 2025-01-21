"""
今有鱉臑下廣五尺，無袤，上袤四尺，無廣，高七尺。問︰積幾何？
術曰：廣袤相乘，以高乘之，六而一。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a truncated pyramid (a frustum). The formula for the volume of a frustum is:

\[
V = \frac{1}{6} \cdot h \cdot (A_1 + A_2 + \sqrt{A_1 \cdot A_2})
\]

Where:
- \( h \) is the height of the frustum,
- \( A_1 \) is the area of the larger base,
- \( A_2 \) is the area of the smaller base.

In this problem:
- The larger base has a width of 5 尺 (chi) and no length (袤), so \( A_1 = 5 \cdot 0 = 0 \).
- The smaller base has a length of 4 尺 and no width, so \( A_2 = 4 \cdot 0 = 0 \).
- The height is 7 尺.

However, since both \( A_1 \) and \( A_2 \) are zero, the volume will also be zero.

Let's compute this in Python:


"""


from fractions import Fraction

# Given dimensions
width_larger_base = Fraction(5)  # 尺
length_larger_base = Fraction(0)  # 尺
width_smaller_base = Fraction(0)  # 尺
length_smaller_base = Fraction(4)  # 尺
height = Fraction(7)  # 尺

# Calculate areas of the bases
A1 = width_larger_base * length_larger_base  # Area of the larger base
A2 = width_smaller_base * length_smaller_base  # Area of the smaller base

# Calculate the volume
a = Fraction(1, 6) * height * (A1 + A2 + (A1 * A2) ** Fraction(1, 2))

# The answer
a  # Volume in 尺


"""


The result is \( a = 0 \) 尺.
"""


"""
Variable 'a' has wrong value. Expected: 70/3, Actual: 0.0"""
