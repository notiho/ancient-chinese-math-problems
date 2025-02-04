"""
今有垣下廣三尺，上廣二尺，高一丈二尺，袤二十二丈五尺八寸。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we will calculate the volume of a trapezoidal prism. The formula provided in the problem can be translated into Python code as follows:

1. Add the bottom width (`垣下廣`) and the top width (`上廣`), then divide by 2 to get the average width.
2. Multiply the average width by the height (`高`).
3. Multiply the result by the length (`袤`).
4. The result is the volume in cubic feet (`積尺`).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
bottom_width = Fraction(3)  # 垣下廣 (3 尺)
top_width = Fraction(2)     # 上廣 (2 尺)
height = Fraction(1 * 10 + 2)  # 高 (1 丈 2 尺 = 12 尺)
length = Fraction(22 * 10 + 5) + Fraction(8, 10)  # 袤 (22 丈 5 尺 8 寸 = 225 尺 8 寸 = 225.8 尺)

# Calculation
average_width = (bottom_width + top_width) / 2  # 平均廣
cross_section_area = average_width * height  # 橫截面積
a = cross_section_area * length  # 積尺 (volume)

# Result
a  # Volume in cubic feet
#----- content ends here -----


"""


The variable `a` will contain the result of the calculation in cubic feet.
"""


"""
"""
