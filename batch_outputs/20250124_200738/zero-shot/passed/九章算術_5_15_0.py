"""
今有圓亭，下周三丈，上周二丈，高一丈。問︰積幾何？
術曰：上、下周相乘，又各自乘，并之，以高乘之，三十六而一。
荅曰： a尺 。
"""

"""
To solve this problem, we will compute the volume of a frustum of a circular cone (a truncated cone). The given dimensions are:

- Bottom circumference (下周): 3丈
- Top circumference (上周): 2丈
- Height (高): 1丈

The formula provided in the problem is:
1. Multiply the bottom circumference by the top circumference.
2. Square each of the circumferences individually and add them together.
3. Multiply the sum by the height.
4. Divide the result by 36.

We will compute the solution step by step in Python. Note that 1丈 = 10尺.


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
bottom_circumference = Fraction(3 * 10)  # Convert 丈 to 尺
top_circumference = Fraction(2 * 10)     # Convert 丈 to 尺
height = Fraction(1 * 10)                # Convert 丈 to 尺

# Step 1: Multiply the bottom and top circumferences
product_of_circumferences = bottom_circumference * top_circumference

# Step 2: Square each circumference and add them together
sum_of_squares = bottom_circumference**2 + top_circumference**2

# Step 3: Add the product of the circumferences to the sum of the squares
combined_sum = product_of_circumferences + sum_of_squares

# Step 4: Multiply by the height
volume_numerator = combined_sum * height

# Step 5: Divide by 36
a = volume_numerator / 36

# The result is stored in variable 'a' in 尺
a
#----- content ends here -----


"""


The variable `a` will contain the volume of the frustum in 尺³.
"""


"""
"""
