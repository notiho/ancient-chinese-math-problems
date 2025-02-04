"""
今有環田，中周九十二步，外周一百二十二步，徑五步。問：為田幾何？
荅曰： a畝 。
"""

"""
Suppose there is a circular ring-shaped field. The inner circumference is 92 bu, and the outer circumference is 122 bu. The width of the ring (diameter of the ring) is 5 bu.
Question: how large is the area of the field?

Answer: *a* mu.
"""

# Inner circumference (中周)
inner_circumference = 92

# Outer circumference (外周)
outer_circumference = 122

# Width of the ring (徑)
width = 5

# Calculate the radius of the inner circle
inner_radius = Fraction(inner_circumference, 2 * 3)  # Using π ≈ 3

# Calculate the radius of the outer circle
outer_radius = Fraction(outer_circumference, 2 * 3)  # Using π ≈ 3

# Calculate the area of the outer circle
outer_area = 3 * outer_radius * outer_radius  # Using π ≈ 3

# Calculate the area of the inner circle
inner_area = 3 * inner_radius * inner_radius  # Using π ≈ 3

# Calculate the area of the ring-shaped field
field_area = outer_area - inner_area

# Convert the area into mu (1 mu = 240 square bu)
a = Fraction(field_area, 240)
"""
"""
