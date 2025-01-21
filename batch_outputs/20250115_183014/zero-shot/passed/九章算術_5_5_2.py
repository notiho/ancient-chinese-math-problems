"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we will calculate the volume of the trapezoidal prism (溝) using the given formula. Here's the Python code:


"""


from fractions import Fraction

# Given dimensions
top_width = Fraction(1, 1) + Fraction(5, 10)  # 1丈5尺 = 1 + 5/10 丈
bottom_width = Fraction(1, 1)  # 1丈
depth = Fraction(5, 10)  # 5尺 = 5/10 丈
length = Fraction(7, 1)  # 7丈

# Formula: ((top_width + bottom_width) / 2) * depth * length
average_width = (top_width + bottom_width) / 2
a = average_width * depth * length  # Volume in cubic 丈

# Convert to cubic 尺 (1 cubic 丈 = 1000 cubic 尺)
a = a * 1000

# The result is stored in variable 'a'


"""


The variable `a` now contains the volume in cubic 尺.
"""


"""
"""
