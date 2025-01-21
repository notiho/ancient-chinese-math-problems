"""
今有塹上廣一丈六尺三寸，下廣一丈，深六尺三寸，袤一十三丈二尺一寸。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we will compute the volume of a trapezoidal prism, which is the shape of the trench described in the problem. The formula provided in the problem is:

1. Add the top width and bottom width, then divide by 2 to get the average width.
2. Multiply the average width by the depth (or height).
3. Multiply the result by the length of the trench to get the total volume in cubic feet.

We will use the class `Fraction` to handle the arithmetic and ensure precision.

Here is the Python code:


"""


from fractions import Fraction

# Given dimensions
top_width = Fraction(1, 1) + Fraction(6, 10) + Fraction(3, 100)  # 1丈6尺3寸
bottom_width = Fraction(1, 1)  # 1丈
depth = Fraction(6, 10) + Fraction(3, 100)  # 6尺3寸
length = Fraction(13, 1) + Fraction(2, 10) + Fraction(1, 100)  # 13丈2尺1寸

# Compute the average width
average_width = (top_width + bottom_width) / 2

# Compute the cross-sectional area
cross_sectional_area = average_width * depth

# Compute the total volume
a = cross_sectional_area * length

# The result is stored in variable 'a' in cubic 尺


"""


### Explanation of Units:
- 1 丈 = 10 尺
- 1 尺 = 10 寸

The result `a` will be the total volume in cubic 尺.
"""


"""
Variable 'a' has wrong value. Expected: 54719/5, Actual: 21887649/2000000"""
