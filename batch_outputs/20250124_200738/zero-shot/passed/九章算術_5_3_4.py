"""
今有隄下廣二丈，上廣八尺，高四尺，袤一十二丈七尺。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we will compute the volume of a trapezoidal prism (representing the structure described). The formula provided in the problem is as follows:

1. Add the top width and bottom width, then divide by 2 to get the average width.
2. Multiply the average width by the height (or depth).
3. Multiply the result by the length to get the total volume in cubic feet.

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
bottom_width = Fraction(2, 1)  # 2丈 (1丈 = 10尺)
top_width = Fraction(8, 10)    # 8尺 (converted to 丈: 8/10丈)
height = Fraction(4, 10)       # 4尺 (converted to 丈: 4/10丈)
length = Fraction(127, 10)     # 12丈7尺 (converted to 丈: 127/10丈)

# Step 1: Compute the average width
average_width = (bottom_width + top_width) / 2

# Step 2: Multiply by the height
cross_section_area = average_width * height

# Step 3: Multiply by the length
a = cross_section_area * length  # Volume in cubic 丈

# Convert the result to cubic 尺 (1 cubic 丈 = 1000 cubic 尺)
a = a * 1000

# The result is stored in variable `a`
#----- content ends here -----


"""


The variable `a` now contains the volume in cubic 尺.
"""


"""
"""
