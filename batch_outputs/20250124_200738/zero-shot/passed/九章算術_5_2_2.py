"""
今有垣下廣三尺，上廣二尺，高一丈二尺，袤二十二丈五尺八寸。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we will calculate the volume of a trapezoidal prism (representing the wall or structure). The formula provided in the problem can be translated into Python code as follows:

1. Add the bottom width ("垣下廣") and the top width ("上廣"), then divide by 2 to get the average width.
2. Multiply the average width by the height ("高").
3. Multiply the result by the length ("袤").
4. The final result is the volume in cubic feet ("積尺").

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
bottom_width = Fraction(3)  # 垣下廣三尺
top_width = Fraction(2)     # 上廣二尺
height = Fraction(1 * 10 + 2)  # 高一丈二尺 (1丈 = 10尺, so 1丈2尺 = 12尺)
length = Fraction(22 * 10 + 5) + Fraction(8, 10)  # 袤二十二丈五尺八寸 (1丈 = 10尺, 1尺 = 10寸)

# Calculate the average width
average_width = (bottom_width + top_width) / 2

# Calculate the volume
a = average_width * height * length  # Volume in cubic feet

# Result
a
#----- content ends here -----


"""


The variable `a` will contain the volume in cubic feet.
"""


"""
"""
