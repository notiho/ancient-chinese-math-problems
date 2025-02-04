"""
今有田從一百步廣四十二步中有圓池周三十步徑一十步。問：池占外為田㡬何？
術曰：列從一百步以廣四十二步乘之得四千二百步為田積又列池周三十步半之得一十五步列徑一十步半之得五步二位相乘得七十五步為池積以減田積餘四千一百二十五步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a rectangular field with a length of 100 bu and a width of 42 bu. 
Within the field, there is a circular pond with a circumference of 30 bu and a diameter of 10 bu.
Question: How much area does the pond occupy, and how much area remains for the field?

The procedure says: 
1. Multiply the length (100 bu) by the width (42 bu) to obtain the total area of the field, 4200 bu².
2. Take the circumference of the pond (30 bu), halve it to get the radius (15 bu).
3. Take the diameter of the pond (10 bu), halve it to get the radius (5 bu).
4. Multiply the two radii (15 bu and 5 bu) to get the area of the pond, 75 bu².
5. Subtract the area of the pond from the total area of the field to get the remaining area, 4125 bu².
6. Divide the remaining area by the mu divisor (240 bu² per mu) to convert it into mu and bu.

Answer: The remaining field area is *a* mu and *b* bu.
"""

from fractions import Fraction

# Field dimensions
length = 100  # bu
width = 42  # bu

# Pond dimensions
circumference = 30  # bu
diameter = 10  # bu

# Mu divisor
mu_divisor = 240  # bu² per mu

# Step 1: Calculate the total area of the field
field_area = length * width  # in bu²

# Step 2: Calculate the radius of the pond from the circumference
radius_from_circumference = Fraction(circumference, 2)  # in bu

# Step 3: Calculate the radius of the pond from the diameter
radius_from_diameter = Fraction(diameter, 2)  # in bu

# Step 4: Calculate the area of the pond
pond_area = radius_from_circumference * radius_from_diameter  # in bu²

# Step 5: Subtract the pond area from the total field area
remaining_area = field_area - pond_area  # in bu²

# Step 6: Convert the remaining area into mu and bu
remaining_mu = remaining_area // mu_divisor  # whole mu
remaining_bu = remaining_area % mu_divisor  # remaining bu

# Final answer
a = remaining_mu
b = remaining_bu

a, b  # Output the result as (a mu, b bu)#----- content ends here -----

"""
"""
