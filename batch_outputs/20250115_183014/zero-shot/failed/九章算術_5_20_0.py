"""
今有鱉臑下廣五尺，無袤，上袤四尺，無廣，高七尺。問︰積幾何？
術曰：廣袤相乘，以高乘之，六而一。
荅曰： a尺 。
"""

"""
To solve this problem, we are calculating the volume of a truncated pyramid (frustum). The formula for the volume of a frustum is given as:

\[
V = \frac{1}{6} \cdot h \cdot (A_1 + A_2 + \sqrt{A_1 \cdot A_2})
\]

Where:
- \( h \) is the height,
- \( A_1 \) is the area of the base,
- \( A_2 \) is the area of the top.

In this problem:
- The base has a width of 5 尺 (A1 = 5 × 5 = 25 尺²),
- The top has a width of 4 尺 (A2 = 4 × 4 = 16 尺²),
- The height is 7 尺.

We will compute the volume step by step.

Here is the Python code:


"""


from fractions import Fraction

# Given dimensions
base_width = 5  # 尺
top_width = 4   # 尺
height = 7      # 尺

# Calculate areas of the base and top
A1 = base_width * base_width  # Base area
A2 = top_width * top_width    # Top area

# Calculate the volume using the formula
a = Fraction(1, 6) * height * (A1 + A2 + (A1 * A2) ** 0.5)

# The result is stored in variable 'a'
a


"""


The variable `a` will contain the volume in 尺³.
"""


"""
Variable 'a' has wrong value. Expected: 70/3, Actual: 71.16666666666667"""
