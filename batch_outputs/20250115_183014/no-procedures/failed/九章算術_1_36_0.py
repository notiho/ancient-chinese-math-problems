"""
今有環田，中周九十二步，外周一百二十二步，徑五步。問：為田幾何？
荅曰： a畝 。
"""

"""
Suppose there is a circular ring-shaped field. The inner circumference is 92 bu, the outer circumference is 122 bu, and the width of the ring is 5 bu.
Question: how large is the area of the field?

Answer: it is *a* mu.
"""

# Inner circumference (中周)
inner_circumference = 92

# Outer circumference (外周)
outer_circumference = 122

# Width of the ring (徑)
width = 5

# Calculate the radii
inner_radius = Fraction(inner_circumference, 2 * 22 / 7)  # r = C / (2π)
outer_radius = Fraction(outer_circumference, 2 * 22 / 7)

# Calculate the areas
inner_area = (22 / 7) * (inner_radius ** 2)  # πr^2 for the inner circle
outer_area = (22 / 7) * (outer_radius ** 2)  # πr^2 for the outer circle

# Area of the ring-shaped field
field_area = outer_area - inner_area

# Convert the area from square bu to mu (1 mu = 240 square bu)
a = Fraction(field_area, 240)
"""
Code error: both arguments should be Rational instances"""
