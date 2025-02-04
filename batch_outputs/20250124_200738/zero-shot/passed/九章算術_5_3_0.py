"""
今有隄下廣二丈，上廣八尺，高四尺，袤一十二丈七尺。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
lower_width = Fraction(2, 1)  # 2丈
upper_width = Fraction(8, 10)  # 8尺 (converted to 丈: 1丈 = 10尺)
height = Fraction(4, 10)  # 4尺 (converted to 丈)
length = Fraction(12, 1) + Fraction(7, 10)  # 12丈7尺 (converted to 丈)

# Formula: ((lower_width + upper_width) / 2) * height * length
a = ((lower_width + upper_width) / 2) * height * length

# The result is in 丈^3, but we need it in 尺^3 (1丈^3 = 1000尺^3)
a = a * 1000

# Output the result
a  # This is the answer in 尺^3
#----- content ends here -----


"""


The variable `a` will contain the answer in cubic 尺 (尺^3).
"""


"""
"""
