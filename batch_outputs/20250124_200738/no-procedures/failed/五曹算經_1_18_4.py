"""
今有田從一百步廣四十二步中有圓池周三十步徑一十步。問：池占外為田㡬何？
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a rectangular field with a length of 100 bu and a width of 42 bu. Inside the field, there is a circular pond with a circumference of 30 bu and a diameter of 10 bu.
Question: How much area of the field remains after accounting for the pond?

Answer: The remaining area is *a* mu and *b* bu².
"""

from fractions import Fraction

# Field dimensions
length = 100  # bu
width = 42  # bu

# Pond dimensions
diameter = 10  # bu
radius = Fraction(diameter, 2)  # radius = diameter / 2
pi = Fraction(22, 7)  # Approximation of π

# Total field area
field_area = length * width  # in bu²

# Pond area (π * r²)
pond_area = pi * radius * radius  # in bu²

# Remaining area
remaining_area = field_area - pond_area  # in bu²

# Convert remaining area to mu and bu²
# 1 mu = 240 bu²
a = remaining_area // 240  # whole mu
b = remaining_area % 240  # remaining bu²

a, b  # Output the result as (a mu, b bu²)#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 45, Actual: 290/7"""
