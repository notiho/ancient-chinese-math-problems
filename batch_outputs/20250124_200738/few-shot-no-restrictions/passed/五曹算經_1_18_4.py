"""
今有田從一百步廣四十二步中有圓池周三十步徑一十步。問：池占外為田㡬何？
術曰：列從一百步以廣四十二步乘之得四千二百步為田積又列池周三十步半之得一十五步列徑一十步半之得五步二位相乘得七十五步為池積以減田積餘四千一百二十五步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a rectangular field with a length of 100 bu and a width of 42 bu. 
Within the field, there is a circular pond with a circumference of 30 bu and a diameter of 10 bu.
Question: how much area does the pond occupy, and how much area remains for the field?

The procedure says:
- Multiply the length (100 bu) by the width (42 bu) to obtain the total field area, 4200 bu².
- For the pond:
  - Take the circumference (30 bu), halve it to get the radius (15 bu).
  - Take the diameter (10 bu), halve it to get the radius (5 bu).
  - Multiply the two radii (15 bu × 5 bu) to obtain the pond area, 75 bu².
- Subtract the pond area from the total field area to get the remaining field area, 4125 bu².
- Divide the remaining area by the mu divisor (240 bu² per mu) to convert it into mu and bu.

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# Field dimensions
length = 100  # bu
width = 42    # bu

# Pond dimensions
circumference = 30  # bu
diameter = 10        # bu

# Mu divisor
mu_divisor = 240  # bu² per mu

# Step 1: Calculate total field area
field_area = length * width  # in bu²

# Step 2: Calculate pond area
radius_from_circumference = Fraction(circumference, 2)  # radius derived from circumference
radius_from_diameter = Fraction(diameter, 2)           # radius derived from diameter
pond_area = radius_from_circumference * radius_from_diameter  # in bu²

# Step 3: Calculate remaining field area
remaining_field_area = field_area - pond_area  # in bu²

# Step 4: Convert remaining field area to mu and bu
remaining_mu = remaining_field_area // mu_divisor  # integer part (mu)
remaining_bu = remaining_field_area % mu_divisor   # remainder (bu)

# Final answer
a = remaining_mu
b = remaining_bu

a, b  # Output the result as (a mu, b bu)#----- content ends here -----

"""
"""
