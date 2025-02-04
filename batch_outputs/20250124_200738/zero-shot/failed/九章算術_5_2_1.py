"""
今有垣下廣三尺，上廣二尺，高一丈二尺，袤二十二丈五尺八寸。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we will calculate the volume of a trapezoidal prism. The formula provided in the problem is:

1. Add the bottom width (`垣下廣`) and the top width (`上廣`), then divide by 2 to get the average width.
2. Multiply the average width by the height (`高`).
3. Multiply the result by the length (`袤`).
4. The result is the volume in cubic feet (積尺).

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
bottom_width = Fraction(3)  # 垣下廣三尺
top_width = Fraction(2)    # 上廣二尺
height = Fraction(1, 1) * 12 + Fraction(2)  # 高一丈二尺 (1丈 = 10尺)
length = Fraction(22, 1) * 10 + Fraction(5) + Fraction(8, 10)  # 袤二十二丈五尺八寸 (1丈 = 10尺, 1尺 = 10寸)

# Calculation
average_width = (bottom_width + top_width) / 2  # Average width
cross_section_area = average_width * height  # Cross-sectional area
a = cross_section_area * length  # Volume in cubic feet

# Result
a
#----- content ends here -----


"""


This will compute the value of `a` in cubic feet.
"""


"""
Variable 'a' has wrong value. Expected: 6774, Actual: 7903"""
