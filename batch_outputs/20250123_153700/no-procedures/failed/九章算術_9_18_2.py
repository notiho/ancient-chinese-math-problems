"""
今有邑方不知大小，各中開門。出北門三十步有木，出西門七百五十步見木。問︰邑方幾何？
荅曰： a里 。
"""

"""
Suppose there is a square city (yi) of unknown size, with gates in the middle of each side.
From the north gate, walking 30 bu leads to a tree. From the west gate, walking 750 bu leads to another tree.
Question: What is the side length of the square city?

Answer: The side length of the city is *a* li.
"""

# Define the known distances
北門距離 = 30  # Distance from the north gate to the tree in bu
西門距離 = 750  # Distance from the west gate to the tree in bu

# The diagonal of the square city is the hypotenuse of a right triangle formed by the distances
# The diagonal is equal to twice the side length of the city (since the gates are in the middle of each side)
# Using the Pythagorean theorem:
# (side_length / 2 + 北門距離)^2 + (side_length / 2 + 西門距離)^2 = (side_length * sqrt(2))^2

from fractions import Fraction

# Let the side length of the city be x
# Equation: ((x / 2) + 30)^2 + ((x / 2) + 750)^2 = x^2
# Expand and simplify:
# (x / 2)^2 + 2 * (x / 2) * 30 + 30^2 + (x / 2)^2 + 2 * (x / 2) * 750 + 750^2 = x^2
# 2 * (x / 2)^2 + x * 30 + 900 + x * 750 + 562500 = x^2
# x^2 / 2 + x * 780 + 563400 = x^2
# x^2 - x^2 / 2 = x * 780 + 563400
# x^2 / 2 = x * 780 + 563400
# Multiply through by 2:
# x^2 = 2 * x * 780 + 2 * 563400
# x^2 = 1560 * x + 1126800
# Rearrange into standard quadratic form:
# x^2 - 1560 * x - 1126800 = 0

# Solve the quadratic equation using the quadratic formula:
# x = (-b ± sqrt(b^2 - 4ac)) / 2a
# Here, a = 1, b = -1560, c = -1126800

a = 1
b = -1560
c = -1126800

# Calculate the discriminant
discriminant = b**2 - 4 * a * c

# Calculate the positive root (since side length must be positive)
side_length_in_bu = (-b + discriminant**0.5) / (2 * a)

# Convert bu to li (1 li = 300 bu)
a = Fraction(side_length_in_bu, 300)

# Final result
a
"""
Code error: both arguments should be Rational instances"""
