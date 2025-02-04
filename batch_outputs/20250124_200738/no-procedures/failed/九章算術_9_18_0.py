"""
今有邑方不知大小，各中開門。出北門三十步有木，出西門七百五十步見木。問︰邑方幾何？
荅曰： a里 。
"""

#----- content starts here -----
"""
Suppose there is a square city of unknown size. Each side of the city has a gate in the middle.
From the north gate, walking 30 bu, there is a tree. From the west gate, walking 750 bu, there is another tree.
Question: What is the side length of the square city?

Answer: The side length of the city is *a* li.
"""

# Definitions:
# 1 li = 300 bu
# Let the side length of the city be x (in bu).

# From the problem, the north gate and west gate distances form a right triangle:
# Half the side length of the city is x/2 (since the gates are in the middle of each side).
# Using the Pythagorean theorem:
# (x/2)^2 + (x/2)^2 = (750 - 30)^2

# Solve for x:
from fractions import Fraction

# Distance from the west gate to the tree minus the north gate to the tree
west_to_tree = 750
north_to_tree = 30
hypotenuse = west_to_tree - north_to_tree

# Equation: (x/2)^2 + (x/2)^2 = hypotenuse^2
# Simplify: 2 * (x/2)^2 = hypotenuse^2
#           x^2 / 2 = hypotenuse^2
#           x^2 = 2 * hypotenuse^2
#           x = sqrt(2 * hypotenuse^2)

x_squared = 2 * (hypotenuse ** 2)
x = Fraction(x_squared).sqrt()

# Convert x from bu to li (1 li = 300 bu)
a = Fraction(x, 300)

# Output the result
a#----- content ends here -----

"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
