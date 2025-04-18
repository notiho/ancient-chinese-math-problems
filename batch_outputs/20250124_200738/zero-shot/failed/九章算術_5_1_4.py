"""
今有城下廣四丈，上廣二丈，高五丈，袤一百二十六丈五尺。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we will calculate the volume (積) of the structure using the given formula. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
lower_width = Fraction(4)  # 四丈
upper_width = Fraction(2)  # 二丈
height = Fraction(5)       # 五丈
length = Fraction(126) + Fraction(5, 10)  # 一百二十六丈五尺 (convert to fractional form)

# Formula: ((lower_width + upper_width) / 2) * height * length
average_width = (lower_width + upper_width) / 2
a = average_width * height * length  # Volume in cubic 尺

# Result
a  # The answer in cubic 尺
#----- content ends here -----


"""


The variable `a` will hold the solution in cubic 尺.
"""


"""
Variable 'a' has wrong value. Expected: 1897500, Actual: 3795/2"""
