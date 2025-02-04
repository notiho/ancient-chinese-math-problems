"""
今有環田，中周九十二步，外周一百二十二步，徑五步。問：為田幾何？
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is a circular ring-shaped field. The inner circumference is 92 bu, and the outer circumference is 122 bu. The width of the ring (diameter of the ring) is 5 bu.
Question: how large is the area of the field?

Answer: *a* mu.
"""

# Inner circumference (中周)
inner_circumference = 92

# Outer circumference (外周)
outer_circumference = 122

# Diameter of the ring (徑)
ring_diameter = 5

# Calculate the radii
inner_radius = Fraction(inner_circumference, 2 * 3)  # Circumference = 2πr, approximate π as 3
outer_radius = Fraction(outer_circumference, 2 * 3)

# Calculate the area of the outer circle and the inner circle
outer_area = 3 * outer_radius * outer_radius  # Area = πr^2, approximate π as 3
inner_area = 3 * inner_radius * inner_radius

# The area of the ring-shaped field is the difference between the outer and inner areas
field_area = outer_area - inner_area

# Convert the area from square bu to mu (1 mu = 240 square bu)
a = Fraction(field_area, 240)  # Convert to mu

a  # Output the result in mu#----- content ends here -----

"""
"""
