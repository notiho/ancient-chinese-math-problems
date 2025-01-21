"""
又有環田，中周六十二步、四分步之三，外周一百一十三步、二分步之一，徑十二步、三分步之二。問：為田幾何？
荅曰： a畝 。
"""

"""
Suppose there is a circular field. The inner circumference is 62 and 3/4 bu, the outer circumference is 113 and 1/2 bu, and the diameter is 12 and 2/3 bu.
Question: how large is the area of the field?

Answer: *a* mu.
"""

from fractions import Fraction

# Inner circumference
inner_circumference = Fraction(62) + Fraction(3, 4)

# Outer circumference
outer_circumference = Fraction(113) + Fraction(1, 2)

# Diameter
diameter = Fraction(12) + Fraction(2, 3)

# Average radius (using the formula: radius = circumference / (2 * pi))
# Approximate pi as 3 for ancient Chinese calculations
pi = 3
inner_radius = inner_circumference / (2 * pi)
outer_radius = outer_circumference / (2 * pi)

# Area of the ring-shaped field (outer area - inner area)
outer_area = pi * (outer_radius ** 2)
inner_area = pi * (inner_radius ** 2)
field_area = outer_area - inner_area

# Convert the area into mu (1 mu = 240 square bu)
a = field_area / 240

a
"""
Variable 'a' has wrong value. Expected: 893/192, Actual: 9541/3072"""
