"""
今有隄下廣二丈，上廣八尺，高四尺，袤一十二丈七尺。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical method into Python code. The problem involves calculating the volume of a trapezoidal prism (a trapezoidal cross-section with a given length). The formula provided in the problem is:

1. Add the top width and bottom width, then divide by 2 to get the average width.
2. Multiply the average width by the height (or depth).
3. Multiply the result by the length to get the volume in cubic feet.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
bottom_width = Fraction(2, 1)  # 2丈 (1丈 = 10尺, so 2丈 = 20尺)
top_width = Fraction(8, 10)    # 8尺 (converted to 丈: 8/10丈)
height = Fraction(4, 10)       # 4尺 (converted to 丈: 4/10丈)
length = Fraction(12, 1) + Fraction(7, 10)  # 12丈7尺 (converted to 丈: 12 + 7/10丈)

# Step 1: Average width
average_width = (bottom_width + top_width) / 2

# Step 2: Cross-sectional area
cross_sectional_area = average_width * height

# Step 3: Volume
a = cross_sectional_area * length  # Volume in cubic 丈

# Convert the result to cubic 尺 (1丈³ = 1000尺³)
a = a * 1000

# The result is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` now contains the volume in cubic 尺.
"""


"""
"""
