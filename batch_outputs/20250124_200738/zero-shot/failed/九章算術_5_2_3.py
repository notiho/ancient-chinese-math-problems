"""
今有垣下廣三尺，上廣二尺，高一丈二尺，袤二十二丈五尺八寸。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a trapezoidal prism. The formula provided in the problem is:

1. Add the bottom width (下廣) and the top width (上廣), then divide by 2 to get the average width.
2. Multiply the average width by the height (高 or 深).
3. Multiply the result by the length (袤).
4. The result is the volume in cubic feet (積尺).

Here is the Python code to compute the value of `a`:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
bottom_width = Fraction(3)  # 下廣 (3尺)
top_width = Fraction(2)     # 上廣 (2尺)
height = Fraction(1 * 10 + 2)  # 高 (1丈2尺 = 12尺)
length = Fraction(22 * 10 + 5 + 8 / 10)  # 袤 (22丈5尺8寸 = 225.8尺)

# Step 1: Compute the average width
average_width = (bottom_width + top_width) / 2

# Step 2: Multiply average width by height
cross_section_area = average_width * height

# Step 3: Multiply by length to get the volume
a = cross_section_area * length

# The result is stored in variable `a`
#----- content ends here -----


"""


The variable `a` will contain the volume in cubic feet (積尺).
"""


"""
Variable 'a' has wrong value. Expected: 6774, Actual: 59584734132436995/8796093022208"""
