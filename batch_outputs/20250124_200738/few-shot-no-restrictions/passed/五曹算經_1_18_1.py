"""
今有田從一百步廣四十二步中有圓池周三十步徑一十步。問：池占外為田㡬何？
術曰：列從一百步以廣四十二步乘之得四千二百步為田積又列池周三十步半之得一十五步列徑一十步半之得五步二位相乘得七十五步為池積以減田積餘四千一百二十五步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a rectangular field with a length of 100 bu and a width of 42 bu. 
Within this field, there is a circular pond with a circumference of 30 bu and a diameter of 10 bu.
Question: how much area does the pond occupy, and how much area remains for the field?

The procedure says:
1. Multiply the length (100 bu) by the width (42 bu) to get the total area of the field, 4200 bu².
2. For the pond:
   - Take the circumference (30 bu) and halve it to get the radius (15 bu).
   - Take the diameter (10 bu) and halve it to get the radius (5 bu).
   - Multiply the two radii (15 bu × 5 bu) to get the area of the pond, 75 bu².
3. Subtract the pond's area from the total field area to get the remaining field area: 4200 bu² - 75 bu² = 4125 bu².
4. Divide the remaining area by the mu conversion factor (240 bu² per mu) to get the result in mu and remaining bu².

Answer: The remaining field area is *a* mu and *b* bu².
"""

from fractions import Fraction

# Field dimensions
length = 100  # bu
width = 42    # bu

# Pond dimensions
circumference = 30  # bu
diameter = 10        # bu

# Step 1: Calculate the total area of the field
field_area = length * width  # in bu²

# Step 2: Calculate the area of the pond
radius_circumference = Fraction(circumference, 2)  # Half of the circumference
radius_diameter = Fraction(diameter, 2)           # Half of the diameter
pond_area = radius_circumference * radius_diameter  # in bu²

# Step 3: Subtract the pond's area from the total field area
remaining_field_area = field_area - pond_area  # in bu²

# Step 4: Convert the remaining area to mu and bu²
mu_conversion = 240  # 1 mu = 240 bu²
remaining_mu = remaining_field_area // mu_conversion  # Integer part (mu)
remaining_bu = remaining_field_area % mu_conversion   # Remainder (bu²)

# Final result
a = remaining_mu
b = remaining_bu

a, b  # Output the result as (mu, bu²)#----- content ends here -----

"""
"""
