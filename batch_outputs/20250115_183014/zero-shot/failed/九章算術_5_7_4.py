"""
今有塹上廣一丈六尺三寸，下廣一丈，深六尺三寸，袤一十三丈二尺一寸。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we will calculate the volume of a trapezoidal prism (塹). The formula provided in the problem is:

1. Add the top width (塹上廣) and the bottom width (塹下廣), then divide by 2 to get the average width.
2. Multiply the average width by the depth (深).
3. Multiply the result by the length (袤) to get the total volume in cubic feet (積尺).

Here is the Python code to compute the value of `a`:


"""


from fractions import Fraction

# Given dimensions
top_width = Fraction(1, 1) + Fraction(6, 10) + Fraction(3, 100)  # 1丈6尺3寸
bottom_width = Fraction(1, 1)  # 1丈
depth = Fraction(6, 10) + Fraction(3, 100)  # 6尺3寸
length = Fraction(13, 1) + Fraction(2, 10) + Fraction(1, 100)  # 13丈2尺1寸

# Step 1: Compute the average width
average_width = (top_width + bottom_width) / 2

# Step 2: Multiply average width by depth
cross_sectional_area = average_width * depth

# Step 3: Multiply by length to get the total volume
a = cross_sectional_area * length

# The result is stored in variable `a`


"""


The variable `a` will contain the volume in cubic feet (積尺).
"""


"""
Variable 'a' has wrong value. Expected: 54719/5, Actual: 21887649/2000000"""
