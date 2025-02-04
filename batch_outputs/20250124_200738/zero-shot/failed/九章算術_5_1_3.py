"""
今有城下廣四丈，上廣二丈，高五丈，袤一百二十六丈五尺。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we will calculate the volume of a trapezoidal prism. The formula provided in the problem can be translated as follows:

1. Add the top width and bottom width.
2. Divide the sum by 2 to get the average width.
3. Multiply the average width by the height (or depth).
4. Multiply the result by the length (袤).
5. The final result is the volume in cubic 尺.

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
bottom_width = Fraction(4)  # 四丈 (4 丈)
top_width = Fraction(2)     # 二丈 (2 丈)
height = Fraction(5)        # 五丈 (5 丈)
length = Fraction(126) + Fraction(5, 10)  # 一百二十六丈五尺 (126 丈 5 尺)

# Calculate the average width
average_width = (bottom_width + top_width) / 2

# Calculate the cross-sectional area
cross_sectional_area = average_width * height

# Calculate the total volume
a = cross_sectional_area * length  # Volume in cubic 尺

# The result is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` will contain the volume in cubic 尺.
"""


"""
Variable 'a' has wrong value. Expected: 1897500, Actual: 3795/2"""
