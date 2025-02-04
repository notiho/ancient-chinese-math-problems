"""
今有覆月田從三十步徑十步。問：為田㡬何？
答曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a circular field (覆月田) with a circumference of 30 bu and a diameter of 10 bu.
Question: how large is the area of the field?

Answer: *a* bu².
"""

# 從三十步 (circumference)
circumference = 30

# 徑十步 (diameter)
diameter = 10

# Calculate the radius
radius = Fraction(diameter, 2)

# Area of a circle is π * r². For ancient Chinese math, π is approximated as 3.
pi = 3

# Calculate the area
a = pi * radius * radius#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 150, Actual: 75"""
