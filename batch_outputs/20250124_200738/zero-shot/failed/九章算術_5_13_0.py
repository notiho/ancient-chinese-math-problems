"""
今有圓堡壔，周四丈八尺，高一丈一尺。問︰積幾何？
術曰：周自相乘，以高乘之，十二而一。
荅曰： a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the volume of a cylindrical object (圓堡壔), given its circumference (周) and height (高). The formula provided is:

1. Square the circumference (周自相乘).
2. Multiply the result by the height (以高乘之).
3. Divide the result by 12 (十二而一).

The result will be the volume in cubic 尺 (cubic chi).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
circumference = Fraction(4 * 10 + 8, 10)  # 4丈8尺 = 48尺
height = Fraction(1 * 10 + 1, 10)         # 1丈1尺 = 11尺

# Calculation
volume = (circumference ** 2) * height / 12

# Answer
a = volume  # Volume in cubic 尺
#----- content ends here -----


"""


The variable `a` will contain the solution in cubic 尺.
"""


"""
Variable 'a' has wrong value. Expected: 2112, Actual: 264/125"""
