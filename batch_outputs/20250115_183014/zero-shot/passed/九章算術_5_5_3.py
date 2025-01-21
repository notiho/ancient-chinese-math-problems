"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we will calculate the volume of a trapezoidal prism (representing the ditch or trench). The formula provided in the problem is as follows:

1. Add the top width (`溝上廣`) and the bottom width (`溝下廣`), then divide by 2 to get the average width.
2. Multiply the average width by the depth (`深`).
3. Multiply the result by the length (`袤`).

The units for the calculation are in "尺" (Chinese feet), so we need to convert all dimensions to "尺" before performing the calculations.

Here is the Python code:


"""


from fractions import Fraction

# Dimensions in 尺
top_width = Fraction(1, 1) * 15  # 1丈5尺 = 15尺
bottom_width = Fraction(1, 1) * 10  # 1丈 = 10尺
depth = Fraction(1, 1) * 5  # 5尺
length = Fraction(1, 1) * 70  # 7丈 = 70尺

# Calculation
average_width = (top_width + bottom_width) / 2
cross_section_area = average_width * depth
a = cross_section_area * length  # Volume in cubic 尺

# The result is stored in variable 'a'


"""


The variable `a` contains the volume of the trench in cubic 尺.
"""


"""
"""
