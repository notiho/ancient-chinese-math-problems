"""
今有溝，廣十丈，深五丈，長二十丈，欲以千尺作一方。問：得幾何？
術曰：置廣一十丈，以深五丈乘之，得五千尺，又以長二十丈乘之，得一百萬尺，以一千除之，即得。
答曰： a 方。
"""

"""
To solve this problem, we will calculate the volume of the ditch (溝) and then determine how many units of 1000 cubic feet (千尺) it contains. Here's the Python code:


"""


from fractions import Fraction

# Given dimensions
width = Fraction(10)  # 廣十丈
depth = Fraction(5)   # 深五丈
length = Fraction(20) # 長二十丈

# Calculate the volume
volume = width * depth * length  # Total volume in cubic feet

# Divide by 1000 to find the number of units of 千尺
a = volume / Fraction(1000)

# The result is stored in variable 'a'


"""


The value of `a` will represent the number of units of 千尺.
"""


"""
Variable 'a' has wrong value. Expected: 1000, Actual: 1"""
