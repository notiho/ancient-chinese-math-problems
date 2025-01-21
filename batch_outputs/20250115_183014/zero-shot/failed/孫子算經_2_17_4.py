"""
今有溝，廣十丈，深五丈，長二十丈，欲以千尺作一方。問：得幾何？
術曰：置廣一十丈，以深五丈乘之，得五千尺，又以長二十丈乘之，得一百萬尺，以一千除之，即得。
答曰： a 方。
"""

"""
To solve this problem, we will calculate the volume of a rectangular prism (溝) with the given dimensions (廣 = 10 丈, 深 = 5 丈, 長 = 20 丈). The volume will then be divided by 1000 (千尺) to determine the number of "方" (a unit of volume). Here's the Python code:


"""


from fractions import Fraction

# Dimensions in 丈
width = Fraction(10)  # 廣
depth = Fraction(5)   # 深
length = Fraction(20) # 長

# Calculate the volume in 尺
volume_in_chi = width * depth * length * 100  # 1 丈 = 10 尺, so multiply by 10^3

# Divide by 1000 to get the volume in 方
a = volume_in_chi / 1000

# The result is stored in variable 'a'


"""


The value of `a` represents the number of "方" (volume units).
"""


"""
Variable 'a' has wrong value. Expected: 1000, Actual: 100"""
