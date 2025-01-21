"""
今有圓堡壔，周四丈八尺，高一丈一尺。問︰積幾何？
術曰：周自相乘，以高乘之，十二而一。
荅曰： a尺 。
"""

"""
To solve this problem, we need to compute the volume of a cylindrical shape (圓堡壔). The problem provides the circumference (周) and height (高) of the cylinder. The formula for the volume of a cylinder is given in the problem as:

\[
\text{Volume} = \frac{\text{Circumference}^2 \times \text{Height}}{12}
\]

Here are the given values:
- Circumference = \(4\) 丈 \(8\) 尺 = \(4 \times 10 + 8 = 48\) 尺 (since \(1\) 丈 = \(10\) 尺)
- Height = \(1\) 丈 \(1\) 尺 = \(1 \times 10 + 1 = 11\) 尺

Now, we compute the volume in Python:


"""


from fractions import Fraction

# Given values
circumference = 48  # in 尺
height = 11  # in 尺

# Formula for volume
a = Fraction(circumference**2 * height, 12)

# The result is stored in variable 'a'
a  # Volume in 尺³


"""


The variable `a` will contain the volume in cubic 尺 (尺³).
"""


"""
"""
