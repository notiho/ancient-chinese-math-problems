"""
今有城下廣四丈，上廣二丈，高五丈，袤一百二十六丈五尺。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we will calculate the volume (積) of the structure described. The formula provided in the problem is:

1. Add the upper width (上廣) and lower width (城下廣), then divide by 2 to get the average width.
2. Multiply the average width by the height (高).
3. Multiply the result by the length (袤).

The dimensions provided are:
- 城下廣 (lower width) = 4 丈
- 上廣 (upper width) = 2 丈
- 高 (height) = 5 丈
- 袤 (length) = 126 丈 5 尺

Note: 1 丈 = 10 尺.

Here is the Python code to compute the answer:


"""

#----- content starts here -----

from fractions import Fraction

# Dimensions
lower_width = Fraction(4 * 10)  # Convert 丈 to 尺
upper_width = Fraction(2 * 10)  # Convert 丈 to 尺
height = Fraction(5 * 10)       # Convert 丈 to 尺
length = Fraction(126 * 10 + 5) # Convert 丈 and 尺 to 尺

# Calculation
average_width = (lower_width + upper_width) / 2
volume = average_width * height * length

# Answer
a = volume  # Volume in 尺
#----- content ends here -----


"""


The variable `a` will contain the volume in 尺.
"""


"""
"""
