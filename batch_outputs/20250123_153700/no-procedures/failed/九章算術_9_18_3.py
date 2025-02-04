"""
今有邑方不知大小，各中開門。出北門三十步有木，出西門七百五十步見木。問︰邑方幾何？
荅曰： a里 。
"""

"""
Suppose there is a square city (yi) of unknown size, with gates in the middle of each side.
Exiting the north gate and walking 30 bu, there is a tree.
Exiting the west gate and walking 750 bu, there is another tree.
Question: What is the side length of the square city?

Answer: The side length of the city is *a* li.
"""

# Given values
北門距離 = 30  # Distance from the north gate to the tree in bu
西門距離 = 750  # Distance from the west gate to the tree in bu

# The diagonal from the north tree to the west tree forms a right triangle with half the side length of the city.
# Let the side length of the city be `邑方` (in bu).
# The diagonal of the square city is the hypotenuse of the triangle.

# Using the Pythagorean theorem:
# (邑方 / 2)^2 + (邑方 / 2)^2 = (北門距離 + 西門距離)^2
# Simplify:
# 2 * (邑方 / 2)^2 = (北門距離 + 西門距離)^2
# (邑方 / 2)^2 = (北門距離 + 西門距離)^2 / 2
# 邑方 = 2 * sqrt((北門距離 + 西門距離)^2 / 2)

from fractions import Fraction

# Calculate the side length in bu
邑方_bu = 2 * Fraction((北門距離 + 西門距離) ** 2, 2).sqrt()

# Convert bu to li (1 li = 300 bu)
a = Fraction(邑方_bu, 300)

a
"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
