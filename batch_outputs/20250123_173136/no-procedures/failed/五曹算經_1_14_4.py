"""
今有覆月田從三十步徑十步。問：為田㡬何？
答曰： a步 。
"""

"""
Suppose there is a circular field (覆月田) with a circumference (從) of 30 bu and a diameter (徑) of 10 bu.
Question: how large is the area of the field?

Answer: *a* bu².
"""

# 從 (circumference) = 30 bu
circumference = 30

# 徑 (diameter) = 10 bu
diameter = 10

# 半徑 (radius) = diameter / 2
radius = Fraction(diameter, 2)

# Area of a circle = (circumference * radius) / 2
a = Fraction(circumference * radius, 2)  # Area in bu²
"""
Variable 'a' has wrong value. Expected: 150, Actual: 75"""
