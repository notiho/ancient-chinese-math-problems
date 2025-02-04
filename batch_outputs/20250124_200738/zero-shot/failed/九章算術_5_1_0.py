"""
今有城下廣四丈，上廣二丈，高五丈，袤一百二十六丈五尺。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we will translate the given ancient Chinese mathematical problem into Python code. The problem involves calculating the volume of a trapezoidal prism. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
lower_width = Fraction(4)  # 城下廣四丈 (lower width = 4丈)
upper_width = Fraction(2)  # 上廣二丈 (upper width = 2丈)
height = Fraction(5)       # 高五丈 (height = 5丈)
length = Fraction(126) + Fraction(5, 10)  # 袤一百二十六丈五尺 (length = 126丈5尺 = 126丈 + 0.5丈)

# Formula: ((lower_width + upper_width) / 2) * height * length
a = ((lower_width + upper_width) / 2) * height * length

# Result
a  # Volume in cubic 尺
#----- content ends here -----


"""


This code calculates the volume of the trapezoidal prism in cubic 尺 (Chinese feet). The variable `a` contains the result.
"""


"""
Variable 'a' has wrong value. Expected: 1897500, Actual: 3795/2"""
