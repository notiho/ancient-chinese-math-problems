"""
又有環田，中周六十二步、四分步之三，外周一百一十三步、二分步之一，徑十二步、三分步之二。問：為田幾何？
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is a circular field. The inner circumference is 62 3/4 bu, the outer circumference is 113 1/2 bu, and the diameter is 12 2/3 bu.
Question: how large is the area of the field?

Answer: *a* mu.
"""

from fractions import Fraction

# Inner circumference (中周)
inner_circumference = Fraction(62) + Fraction(3, 4)

# Outer circumference (外周)
outer_circumference = Fraction(113) + Fraction(1, 2)

# Diameter (徑)
diameter = Fraction(12) + Fraction(2, 3)

# Radius (半徑) is half of the diameter
radius = diameter / 2

# Average circumference (平均周)
average_circumference = (inner_circumference + outer_circumference) / 2

# Area of the circular field (田面積) = (average_circumference * radius) / 2
area_in_bu = (average_circumference * radius) / 2

# Convert area from bu to mu (1 mu = 240 bu)
a = area_in_bu / 240

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 893/192, Actual: 893/768"""
