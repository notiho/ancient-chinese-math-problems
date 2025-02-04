"""
今有溝，廣十丈，深五丈，長二十丈，欲以千尺作一方。問：得幾何？
術曰：置廣一十丈，以深五丈乘之，得五千尺，又以長二十丈乘之，得一百萬尺，以一千除之，即得。
答曰： a 方。
"""

"""
To solve this problem, we will compute the volume of a rectangular prism (溝) with given dimensions (廣, 深, 長) and then divide the total volume by 1000 to determine how many units of "方" (a unit of volume) it contains. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Dimensions of the rectangular prism
廣 = 10  # in 丈
深 = 5   # in 丈
長 = 20  # in 丈

# Compute the volume in cubic 丈
體積 = 廣 * 深 * 長  # Volume in cubic 丈

# Convert to 方 by dividing by 1000
a = Fraction(體積, 1000)  # Result in 方

# The answer is stored in variable 'a'
#----- content ends here -----


"""


The solution is stored in the variable `a` as a fraction in units of 方.
"""


"""
Variable 'a' has wrong value. Expected: 1000, Actual: 1"""
