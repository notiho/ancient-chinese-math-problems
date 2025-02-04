"""
今有溝，廣十丈，深五丈，長二十丈，欲以千尺作一方。問：得幾何？
術曰：置廣一十丈，以深五丈乘之，得五千尺，又以長二十丈乘之，得一百萬尺，以一千除之，即得。
答曰： a 方。
"""

"""
To solve the problem, we will compute the volume of the ditch (溝) and then divide it by 1000 to determine how many "方" (units of 1000 cubic 尺) it contains.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions of the ditch
width = Fraction(10)  # 廣十丈
depth = Fraction(5)   # 深五丈
length = Fraction(20) # 長二十丈

# Compute the volume in cubic 尺
volume = width * depth * length  # Volume in cubic 尺

# Divide by 1000 to convert to 方
a = volume / Fraction(1000)

# The answer is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` will contain the number of 方.
"""


"""
Variable 'a' has wrong value. Expected: 1000, Actual: 1"""
