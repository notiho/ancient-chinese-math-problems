"""
今有芻甍，下廣三丈，袤四丈，上袤二丈，無廣，高一丈。問︰積幾何？
術曰：倍下袤，上袤從之，以廣乘之，又以高乘之，六而一。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a frustum-like structure (trapezoidal prism). Here's the Python code to compute the value of `a`:


"""


from fractions import Fraction

# Given dimensions
lower_width = Fraction(3 * 10)  # Convert from 丈 to 尺 (1 丈 = 10 尺)
lower_length = Fraction(4 * 10)  # Convert from 丈 to 尺
upper_length = Fraction(2 * 10)  # Convert from 丈 to 尺
height = Fraction(1 * 10)  # Convert from 丈 to 尺

# Calculation
double_lower_length = lower_length * 2
sum_lengths = double_lower_length + upper_length
area_base = sum_lengths * lower_width
volume = area_base * height / 6

# Answer
a = volume  # Volume in cubic 尺


"""


The value of `a` will represent the volume in cubic 尺.
"""


"""
"""
