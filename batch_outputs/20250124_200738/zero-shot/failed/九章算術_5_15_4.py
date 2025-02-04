"""
今有圓亭，下周三丈，上周二丈，高一丈。問︰積幾何？
術曰：上、下周相乘，又各自乘，并之，以高乘之，三十六而一。
荅曰： a尺 。
"""

"""
To solve this problem, we will calculate the volume of a frustum (truncated cone) based on the given dimensions. The formula for the volume of a frustum is derived from the ancient Chinese method described in the problem:

1. Multiply the upper circumference (上周) and the lower circumference (下周).
2. Square each of the upper and lower circumferences, then add them together.
3. Multiply the result by the height (高).
4. Divide the entire result by 36.

The units are given in 丈 (zhang), and the final answer will be converted to 尺 (chi), where 1 丈 = 10 尺.

Here is the Python code to compute the answer:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
lower_circumference = Fraction(3)  # 下周三丈 (3 丈)
upper_circumference = Fraction(2)  # 上周二丈 (2 丈)
height = Fraction(1)  # 高一丈 (1 丈)

# Step 1: Multiply the upper and lower circumferences
product_of_circumferences = lower_circumference * upper_circumference

# Step 2: Square each circumference and add them together
sum_of_squares = lower_circumference**2 + upper_circumference**2

# Step 3: Add the product of the circumferences to the sum of squares
combined_value = product_of_circumferences + sum_of_squares

# Step 4: Multiply by the height
volume_in_zhang = combined_value * height

# Step 5: Divide by 36
volume_in_zhang /= 36

# Convert the volume to 尺 (1 丈 = 10 尺)
a = volume_in_zhang * 10

# The result is stored in variable 'a' in 尺
#----- content ends here -----


"""


The variable `a` now contains the volume of the frustum in 尺.
"""


"""
Variable 'a' has wrong value. Expected: 4750/9, Actual: 95/18"""
