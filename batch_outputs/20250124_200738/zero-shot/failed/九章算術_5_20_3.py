"""
今有鱉臑下廣五尺，無袤，上袤四尺，無廣，高七尺。問︰積幾何？
術曰：廣袤相乘，以高乘之，六而一。
荅曰： a尺 。
"""

"""
To solve this problem, we need to compute the volume of a truncated pyramid (frustum). The formula for the volume of a frustum is:

\[
V = \frac{1}{6} \cdot h \cdot (A_1 + A_2 + \sqrt{A_1 \cdot A_2})
\]

Where:
- \( h \) is the height of the frustum.
- \( A_1 \) is the area of the base.
- \( A_2 \) is the area of the top.

In this problem:
- The base has a width of 5 feet (\( A_1 = 5 \times 5 = 25 \)).
- The top has a width of 4 feet (\( A_2 = 4 \times 4 = 16 \)).
- The height is 7 feet (\( h = 7 \)).

Now, let's compute the volume in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
base_width = 5  # feet
top_width = 4   # feet
height = 7      # feet

# Compute areas of the base and top
A1 = base_width * base_width  # Area of the base
A2 = top_width * top_width    # Area of the top

# Compute the volume using the formula
a = Fraction(1, 6) * height * (A1 + A2 + (A1 * A2) ** 0.5)

# The result is stored in variable 'a'
a
#----- content ends here -----


"""


The variable `a` will contain the volume of the frustum in cubic feet.
"""


"""
Variable 'a' has wrong value. Expected: 70/3, Actual: 71.16666666666667"""
