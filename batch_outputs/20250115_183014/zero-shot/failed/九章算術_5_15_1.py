"""
今有圓亭，下周三丈，上周二丈，高一丈。問︰積幾何？
術曰：上、下周相乘，又各自乘，并之，以高乘之，三十六而一。
荅曰： a尺 。
"""

"""
To solve the problem, we will compute the volume of the frustum of a circular cone (圓亭). The formula provided in the problem can be interpreted as follows:

1. Multiply the upper circumference (上周) by the lower circumference (下周).
2. Square each of the circumferences individually and add them together.
3. Multiply the result by the height (高).
4. Divide the entire result by 36.

The given dimensions are:
- 下周 (lower circumference) = 3 丈
- 上周 (upper circumference) = 2 丈
- 高 (height) = 1 丈

We will compute the volume step by step and store the result in the variable `a`.

Here is the Python code:


"""


from fractions import Fraction

# Given dimensions
lower_circumference = Fraction(3)  # 丈
upper_circumference = Fraction(2)  # 丈
height = Fraction(1)  # 丈

# Step 1: Multiply the upper and lower circumferences
product_of_circumferences = lower_circumference * upper_circumference

# Step 2: Square each circumference and add them together
sum_of_squares = lower_circumference**2 + upper_circumference**2

# Step 3: Add the product of the circumferences to the sum of squares
combined_sum = product_of_circumferences + sum_of_squares

# Step 4: Multiply by the height
volume_numerator = combined_sum * height

# Step 5: Divide the result by 36
a = volume_numerator / Fraction(36)

# The result is stored in variable `a` (in 丈³)


"""


The variable `a` will contain the volume of the frustum in cubic 丈 (丈³).
"""


"""
Variable 'a' has wrong value. Expected: 4750/9, Actual: 19/36"""
