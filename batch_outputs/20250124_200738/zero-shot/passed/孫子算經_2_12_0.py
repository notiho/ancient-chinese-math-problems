"""
今有圓田周三百步，徑一百步。問：得田幾何？
術曰：先置周三百步，半之，得一百五十步；又置徑一百步半之，得五十步，相乘，得七千五百步，以畝法二百四十步除之，即得。
答曰： a畝 ，奇 b步 。
"""

"""
To solve this problem, we will compute the area of a circular field given its circumference and diameter. The area is calculated using the formula for the area of a circle, but in this ancient problem, the method involves approximating the area by multiplying half the circumference by half the diameter.

Here is the Python code to compute the values of `a` (whole acres) and `b` (remaining steps):


"""

#----- content starts here -----

from fractions import Fraction

# Given values
circumference = 300  # 周, in steps
diameter = 100       # 徑, in steps
area_per_mu = 240    # 畝法, 1 畝 = 240 steps

# Calculations
half_circumference = Fraction(circumference, 2)  # 半周
half_diameter = Fraction(diameter, 2)           # 半徑
total_area = half_circumference * half_diameter # 總面積 in steps

# Convert total area into 畝 and remaining steps
a = total_area // area_per_mu  # Whole 畝
b = total_area % area_per_mu   # Remaining steps

# Results
a, b
#----- content ends here -----


"""


This code will calculate the values of `a` (whole acres) and `b` (remaining steps).
"""


"""
"""
