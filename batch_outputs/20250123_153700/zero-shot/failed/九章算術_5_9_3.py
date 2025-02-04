"""
今有穿渠上廣一丈八尺，下廣三尺六寸，深一丈八尺，袤五萬一千八百二十四尺。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we will calculate the volume of the trapezoidal prism (representing the canal). The formula provided in the problem can be translated into Python code as follows:

1. Add the top width and bottom width, then take half of the sum.
2. Multiply the result by the depth (or height).
3. Multiply the result by the length (袤).
4. The final result is the volume in cubic feet (積尺).

Here is the Python code:


"""


from fractions import Fraction

# Given dimensions
top_width = Fraction(1, 1) * 8  # 1丈8尺 = 18尺
bottom_width = Fraction(3, 1) * 6  # 3尺6寸 = 3.6尺
depth = Fraction(1, 1) * 8  # 1丈8尺 = 18尺
length = Fraction(51824, 1)  # 51824尺

# Calculation
average_width = (top_width + bottom_width) / 2
cross_section_area = average_width * depth
a = cross_section_area * length  # Volume in cubic feet

# The result is stored in variable 'a'


"""


After running this code, the variable `a` will contain the volume of the canal in cubic feet.
"""


"""
Variable 'a' has wrong value. Expected: 50372928/5, Actual: 5389696"""
