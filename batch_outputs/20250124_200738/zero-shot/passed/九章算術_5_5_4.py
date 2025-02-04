"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we will compute the volume of a trapezoidal prism (溝). The formula provided in the problem can be translated into Python code as follows:

1. Add the top width (上廣) and bottom width (下廣), then divide by 2 to get the average width.
2. Multiply the average width by the depth (深).
3. Multiply the result by the length (袤).
4. The final result is the volume in cubic 尺.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
top_width = Fraction(1, 1) * 15  # 1丈5尺 = 15尺
bottom_width = Fraction(1, 1) * 10  # 1丈 = 10尺
depth = Fraction(1, 1) * 5  # 5尺
length = Fraction(1, 1) * 70  # 7丈 = 70尺

# Calculate the average width
average_width = (top_width + bottom_width) / 2

# Calculate the cross-sectional area
cross_sectional_area = average_width * depth

# Calculate the volume
a = cross_sectional_area * length

# The result is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` will contain the volume in cubic 尺.
"""


"""
"""
