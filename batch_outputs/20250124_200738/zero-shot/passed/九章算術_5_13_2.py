"""
今有圓堡壔，周四丈八尺，高一丈一尺。問︰積幾何？
術曰：周自相乘，以高乘之，十二而一。
荅曰： a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the volume of a cylinder (圓堡壔), where the formula provided is:

1. Multiply the circumference (周) by itself.
2. Multiply the result by the height (高).
3. Divide the final result by 12.

The given dimensions are:
- Circumference (周) = 4丈8尺 = 48尺 (since 1丈 = 10尺)
- Height (高) = 1丈1尺 = 11尺

We will compute the volume (積) in cubic 尺.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
circumference = 48  # in 尺
height = 11  # in 尺

# Compute the volume
a = Fraction(circumference * circumference * height, 12)

# The result is stored in variable 'a'
a  # in cubic 尺
#----- content ends here -----


"""


The variable `a` will contain the volume of the cylinder in cubic 尺.
"""


"""
"""
