"""
今有覆月田從三十步徑十步。問：為田㡬何？
答曰： a步 。
"""

"""
Suppose there is a circular field (覆月田) with a circumference of 30 bu and a diameter of 10 bu.
Question: how large is the area of the field?

Answer: *a* bu².
"""

# 從 (circumference) = 30 步
circumference = 30

# 徑 (diameter) = 10 步
diameter = 10

# 半徑 (radius) = diameter / 2
radius = Fraction(diameter, 2)

# Area of a circle = π * r²
# Ancient Chinese approximation for π = 3
pi = 3

# Calculate the area
a = pi * radius * radius  # a is the area in square bu

a
"""
Variable 'a' has wrong value. Expected: 150, Actual: 75"""
