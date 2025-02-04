"""
今有田從一百步廣四十二步中有圓池周三十步徑一十步。問：池占外為田㡬何？
術曰：列從一百步以廣四十二步乘之得四千二百步為田積又列池周三十步半之得一十五步列徑一十步半之得五步二位相乘得七十五步為池積以減田積餘四千一百二十五步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a rectangular field with a length of 100 bu and a width of 42 bu. Inside the field, there is a circular pond with a circumference of 30 bu and a diameter of 10 bu.
Question: How much area of the field remains after accounting for the pond?

The procedure says: 
1. Multiply the length (100 bu) by the width (42 bu) to obtain the total area of the field.
2. Divide the circumference of the pond (30 bu) by 2 to get the radius (15 bu).
3. Divide the diameter of the pond (10 bu) by 2 to get the radius (5 bu).
4. Multiply the radius by itself and by π (approximated as 3) to calculate the area of the pond.
5. Subtract the pond's area from the total field area to get the remaining area.
6. Divide the remaining area by the mu conversion factor (240 bu² per mu) to get the result in mu and bu.

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# Field dimensions
length = 100  # bu
width = 42  # bu

# Pond dimensions
circumference = 30  # bu
diameter = 10  # bu

# Mu conversion factor
mu_conversion = 240  # bu² per mu

# Step 1: Calculate the total area of the field
field_area = length * width  # in bu²

# Step 2: Calculate the radius of the pond
radius = Fraction(diameter, 2)  # radius = diameter / 2

# Step 3: Calculate the area of the pond (using π ≈ 3)
pond_area = 3 * radius * radius  # in bu²

# Step 4: Subtract the pond's area from the field's area
remaining_area = field_area - pond_area  # in bu²

# Step 5: Convert the remaining area into mu and bu
mu = remaining_area // mu_conversion  # integer part (mu)
bu = remaining_area % mu_conversion  # remainder (bu)

# Final answer
a = mu
b = bu

a, b  # Output the result as (mu, bu)#----- content ends here -----

"""
"""
