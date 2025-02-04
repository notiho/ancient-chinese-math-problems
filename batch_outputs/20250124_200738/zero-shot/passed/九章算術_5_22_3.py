"""
今有芻甍，下廣三丈，袤四丈，上袤二丈，無廣，高一丈。問︰積幾何？
術曰：倍下袤，上袤從之，以廣乘之，又以高乘之，六而一。
荅曰： a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the volume of a frustum of a rectangular pyramid. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
lower_width = Fraction(3 * 10)  # Convert 3丈 to 尺 (1丈 = 10尺)
lower_length = Fraction(4 * 10)  # Convert 4丈 to 尺
upper_length = Fraction(2 * 10)  # Convert 2丈 to 尺
height = Fraction(1 * 10)  # Convert 1丈 to 尺

# Calculation
volume = (2 * lower_length + upper_length) * lower_width * height / 6

# Solution
a = volume  # Volume in 尺³
#----- content ends here -----


"""


The variable `a` will hold the volume of the frustum in cubic 尺 (尺³).
"""


"""
"""
