"""
今有田從一百步廣四十二步中有圓池周三十步徑一十步。問：池占外為田㡬何？
術曰：列從一百步以廣四十二步乘之得四千二百步為田積又列池周三十步半之得一十五步列徑一十步半之得五步二位相乘得七十五步為池積以減田積餘四千一百二十五步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a rectangular field with a length of 100 bu and a width of 42 bu. Inside the field, there is a circular pond with a circumference of 30 bu and a diameter of 10 bu.
Question: How much of the field is occupied by the pond, and how much remains as usable field?

The procedure says: 
- Multiply the length (100 bu) by the width (42 bu) to obtain the total area of the field, 4200 bu².
- For the pond, take the circumference (30 bu), halve it to get the radius (15 bu).
- Take the diameter (10 bu), halve it to get the radius (5 bu).
- Multiply the radius by itself (5 × 5 = 25), then multiply by π (approximated as 3) to get the area of the pond (75 bu²).
- Subtract the pond's area from the total field area to get the remaining field area (4200 - 75 = 4125 bu²).
- Divide the remaining area by the mu divisor (240 bu² per mu) to convert to mu and bu.

Answer: The remaining field is *a* mu and *b* bu.
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

# Step 1: Calculate the total area of the field
field_area = length * width  # in bu²

# Step 2: Calculate the radius of the pond
radius = Fraction(diameter, 2)  # radius = diameter / 2

# Step 3: Calculate the area of the pond
pond_area = 3 * (radius ** 2)  # π approximated as 3

# Step 4: Subtract the pond's area from the field's area
remaining_area = field_area - pond_area  # in bu²

# Step 5: Convert the remaining area to mu and bu
remaining_mu = remaining_area // mu_divisor  # integer part (mu)
remaining_bu = remaining_area % mu_divisor   # remainder (bu)

# Final answer
a = remaining_mu  # mu
b = remaining_bu  # bu

a, b  # Output the result#----- content ends here -----

"""
"""
