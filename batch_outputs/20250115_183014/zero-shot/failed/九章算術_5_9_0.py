"""
今有穿渠上廣一丈八尺，下廣三尺六寸，深一丈八尺，袤五萬一千八百二十四尺。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the volume of a trapezoidal prism (a canal) with given dimensions. The formula provided in the problem is:

1. Add the top width and bottom width, then divide by 2 to get the average width.
2. Multiply the average width by the depth (or height).
3. Multiply the result by the length to get the total volume in cubic feet.

Here is the Python code:


"""


from fractions import Fraction

# Given dimensions
top_width = Fraction(1, 1) * 18  # 1丈8尺 = 18尺
bottom_width = Fraction(3, 1) * 6  # 3尺6寸 = 3.6尺
depth = Fraction(1, 1) * 18  # 1丈8尺 = 18尺
length = Fraction(51824, 1)  # 51824尺

# Calculation
average_width = (top_width + bottom_width) / 2
cross_sectional_area = average_width * depth
a = cross_sectional_area * length  # Volume in cubic 尺

# The result is stored in variable 'a'


"""


The variable `a` will contain the total volume in cubic 尺.
"""


"""
Variable 'a' has wrong value. Expected: 50372928/5, Actual: 16790976"""
