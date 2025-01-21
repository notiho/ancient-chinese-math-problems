"""
今有隄下廣二丈，上廣八尺，高四尺，袤一十二丈七尺。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the volume of a trapezoidal prism. Here's the solution:


"""


from fractions import Fraction

# Given dimensions
lower_width = Fraction(2)  # 2丈 (1丈 = 10尺)
upper_width = Fraction(8, 10)  # 8尺 (converted to 丈)
height = Fraction(4, 10)  # 4尺 (converted to 丈)
length = Fraction(12) + Fraction(7, 10)  # 12丈 7尺 (converted to 丈)

# Formula: ((lower_width + upper_width) / 2) * height * length
a = ((lower_width + upper_width) / 2) * height * length

# The result is stored in variable 'a'
a  # Volume in cubic 尺


"""


### Explanation:
1. **Units Conversion**: All measurements are converted to 丈 for consistency since 1丈 = 10尺.
2. **Trapezoidal Prism Volume Formula**: The formula is derived from the ancient method:
   - Average the lower and upper widths: `(lower_width + upper_width) / 2`.
   - Multiply by the height (or depth).
   - Multiply by the length.
3. **Result**: The volume is stored in the variable `a` in cubic 尺.
"""


"""
Variable 'a' has wrong value. Expected: 7112, Actual: 889/125"""
