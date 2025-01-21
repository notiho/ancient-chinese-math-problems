"""
今有城下廣四丈，上廣二丈，高五丈，袤一百二十六丈五尺。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the volume of a trapezoidal prism, where the base and top widths, height, and length are given. The formula provided is:

1. Add the top and bottom widths.
2. Divide the sum by 2 to get the average width.
3. Multiply the average width by the height (or depth).
4. Multiply the result by the length to get the volume.

Here is the Python code:


"""


from fractions import Fraction

# Given values
bottom_width = Fraction(4)  # Bottom width in 丈
top_width = Fraction(2)     # Top width in 丈
height = Fraction(5)        # Height in 丈
length = Fraction(126) + Fraction(5, 10)  # Length in 丈 (126丈5尺 = 126.5丈)

# Calculation
average_width = (bottom_width + top_width) / 2
cross_section_area = average_width * height
a = cross_section_area * length  # Volume in cubic 丈

# Convert to cubic 尺 (1 cubic 丈 = 1000 cubic 尺)
a *= 1000

# The answer is stored in variable 'a'


"""


After running this code, the variable `a` will contain the volume in cubic 尺.
"""


"""
"""
