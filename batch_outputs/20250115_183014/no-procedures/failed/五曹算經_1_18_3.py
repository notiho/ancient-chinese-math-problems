"""
今有田從一百步廣四十二步中有圓池周三十步徑一十步。問：池占外為田㡬何？
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a rectangular field with a length of 100 bu and a width of 42 bu. Inside the field, there is a circular pond with a circumference of 30 bu and a diameter of 10 bu.
Question: how much area does the pond occupy, and how much area remains as usable field?

Answer: The pond occupies *a* mu and *b* bu², and the remaining field area is calculated accordingly.
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

# Remaining field area
remaining_field_area = field_area - pond_area  # in bu²

# Convert pond area to mu and bu²
pond_area_mu = pond_area // 240  # 1 mu = 240 bu²
pond_area_bu = pond_area % 240  # Remaining bu²

# Convert remaining field area to mu and bu²
remaining_field_mu = remaining_field_area // 240  # 1 mu = 240 bu²
remaining_field_bu = remaining_field_area % 240  # Remaining bu²

# Output results
a_mu = pond_area_mu
b_bu = pond_area_bu

a_mu_remaining = remaining_field_mu
b_bu_remaining = remaining_field_bu

# Results
a_mu, b_bu, a_mu_remaining, b_bu_remaining
"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
