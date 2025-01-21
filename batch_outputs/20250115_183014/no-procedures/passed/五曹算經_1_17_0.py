"""
今有環田外周三十步內周一十二步徑三步。問：為田㡬何？
答曰： a步 。
"""

"""
Suppose there is a circular field with an outer circumference of 30 bu, an inner circumference of 12 bu, and the width of the ring (the difference between the outer and inner radii) is 3 bu.
Question: how much area does the field cover?

Answer: *a* bu².
"""

# Importing Fraction for precise calculations
from fractions import Fraction

# Given values
outer_circumference = 30  # Outer circumference in bu
inner_circumference = 12  # Inner circumference in bu
width = 3  # Width of the ring in bu

# Calculate the radii
outer_radius = Fraction(outer_circumference, 2 * 3)  # r_outer = C_outer / (2π), approximating π as 3
inner_radius = Fraction(inner_circumference, 2 * 3)  # r_inner = C_inner / (2π)

# Calculate the area of the outer circle and inner circle
outer_area = 3 * outer_radius**2  # Area = πr², approximating π as 3
inner_area = 3 * inner_radius**2  # Area = πr², approximating π as 3

# The area of the ring-shaped field
a = outer_area - inner_area  # Subtract the inner circle area from the outer circle area

a  # Result in bu²
"""
"""
