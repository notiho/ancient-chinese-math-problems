"""
今有圓田周三百步，徑一百步。問：得田幾何？
術曰：先置周三百步，半之，得一百五十步；又置徑一百步半之，得五十步，相乘，得七千五百步，以畝法二百四十步除之，即得。
答曰： a畝 ，奇 b步 。
"""

"""
To solve this problem, we will compute the area of a circular field given its circumference and diameter. The area of a circle can be calculated using the formula:

\[
\text{Area} = \frac{\text{Circumference} \times \text{Radius}}{2}
\]

Here, the circumference is 300 steps, and the diameter is 100 steps. The radius is half the diameter. The area in steps will then be converted to "畝" (a traditional Chinese unit of area) using the conversion factor: 1 畝 = 240 steps.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
circumference = 300  # in steps
diameter = 100  # in steps

# Calculations
radius = Fraction(diameter, 2)  # Radius is half the diameter
area_in_steps = Fraction(circumference * radius, 2)  # Area in steps
a = area_in_steps // 240  # Full 畝
b = area_in_steps % 240  # Remaining steps

# Results
a, b
#----- content ends here -----


"""


This will compute the values of `a` (畝) and `b` (remaining steps).
"""


"""
"""
