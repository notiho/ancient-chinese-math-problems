"""
又有環田，中周六十二步、四分步之三，外周一百一十三步、二分步之一，徑十二步、三分步之二。問：為田幾何？
荅曰： a畝 。
"""

"""
Suppose there is a circular field. The inner circumference is 62 bu and 3/4 bu, the outer circumference is 113 bu and 1/2 bu, and the diameter is 12 bu and 2/3 bu.
Question: how large is the area of the field?

Answer: it is *a* mu.
"""

from fractions import Fraction

# 中周 (inner circumference)
inner_circumference = 62 + Fraction(3, 4)

# 外周 (outer circumference)
outer_circumference = 113 + Fraction(1, 2)

# 徑 (diameter)
diameter = 12 + Fraction(2, 3)

# Calculate the radius (半徑 = diameter / 2)
radius = diameter / 2

# Calculate the area of the circular field using the formula:
# Area = (inner_circumference + outer_circumference) / 2 * radius
area_in_bu = (inner_circumference + outer_circumference) / 2 * radius

# Convert the area from bu^2 to mu (1 mu = 240 bu^2)
a = Fraction(area_in_bu, 240)

a
"""
Variable 'a' has wrong value. Expected: 893/192, Actual: 893/384"""
