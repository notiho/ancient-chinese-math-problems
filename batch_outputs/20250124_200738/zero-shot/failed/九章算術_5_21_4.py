"""
今有羨除，下廣六尺，上廣一丈，深三尺，末廣八尺，無深，袤七尺。問︰積幾何？
術曰：并三廣，以深乘之，又以袤乘之，六而一。
荅曰： a尺 。
"""

"""
To solve this problem, let's translate the ancient Chinese math problem into Python code. The problem describes a frustum-like shape with specific dimensions, and we are tasked with calculating its volume. The formula provided in the problem is to average the three widths (lower width, upper width, and middle width), multiply by the depth, and then multiply by the length.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
lower_width = Fraction(6)  # 6 尺
upper_width = Fraction(10)  # 1 丈 = 10 尺
middle_width = Fraction(8)  # 8 尺
depth = Fraction(3)  # 3 尺
length = Fraction(7)  # 7 尺

# Calculate the average of the three widths
average_width = (lower_width + upper_width + middle_width) / 3

# Calculate the volume
a = average_width * depth * length

# Result
a  # Volume in cubic 尺
#----- content ends here -----


"""


The variable `a` will contain the volume of the shape in cubic 尺.
"""


"""
Variable 'a' has wrong value. Expected: 84, Actual: 168"""
