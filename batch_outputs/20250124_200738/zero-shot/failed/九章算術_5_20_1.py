"""
今有鱉臑下廣五尺，無袤，上袤四尺，無廣，高七尺。問︰積幾何？
術曰：廣袤相乘，以高乘之，六而一。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a frustum of a pyramid (truncated pyramid). The formula for the volume of a frustum is given by:

\[
V = \frac{1}{6} \cdot h \cdot (A_1 + A_2 + \sqrt{A_1 \cdot A_2})
\]

Where:
- \( h \) is the height of the frustum,
- \( A_1 \) is the area of the bottom base,
- \( A_2 \) is the area of the top base.

In this problem:
- The bottom base has a width of 5 尺 (A1 = 5² = 25 square 尺),
- The top base has a width of 4 尺 (A2 = 4² = 16 square 尺),
- The height is 7 尺.

We will compute the volume step by step.


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
bottom_width = 5  # 尺
top_width = 4     # 尺
height = 7        # 尺

# Calculate areas of the bases
A1 = bottom_width ** 2  # Area of the bottom base
A2 = top_width ** 2     # Area of the top base

# Calculate the volume using the formula
a = Fraction(1, 6) * height * (A1 + A2 + (A1 * A2) ** 0.5)

# The answer is stored in variable 'a'
a  # Volume in cubic 尺
#----- content ends here -----


"""


This code calculates the volume of the frustum in cubic 尺 and stores the result in the variable `a`.
"""


"""
Variable 'a' has wrong value. Expected: 70/3, Actual: 71.16666666666667"""
