"""
今有戶高多於廣六尺八寸，兩隅相去適一丈。問︰戶高、廣各幾何？
荅曰：廣 a尺 ；高 b尺 。
"""

"""
Suppose there is a door where the height exceeds the width by 6 chi and 8 cun. The diagonal distance between the two opposite corners is exactly 10 chi.
Question: what are the width and height of the door?

Answer: the width is *a* chi, and the height is *b* chi.
"""

# Definitions
diagonal = 10  # diagonal distance in chi
height_minus_width = 6 + Fraction(8, 10)  # height exceeds width by 6 chi and 8 cun

# Using the Pythagorean theorem: diagonal^2 = width^2 + height^2
# Let width = x, then height = x + height_minus_width
# Solve: diagonal^2 = x^2 + (x + height_minus_width)^2

from fractions import Fraction

# Define the equation
diagonal_squared = diagonal ** 2
height_minus_width_squared = height_minus_width ** 2

# Solve for width (x)
# diagonal^2 = x^2 + (x + height_minus_width)^2
# diagonal^2 = x^2 + x^2 + 2 * x * height_minus_width + height_minus_width^2
# 0 = 2 * x^2 + 2 * x * height_minus_width + height_minus_width^2 - diagonal^2
# Solve the quadratic equation: ax^2 + bx + c = 0
a = 2
b = 2 * height_minus_width
c = height_minus_width_squared - diagonal_squared

# Quadratic formula: x = (-b ± sqrt(b^2 - 4ac)) / 2a
discriminant = b ** 2 - 4 * a * c
sqrt_discriminant = discriminant ** 0.5

# Calculate width (x)
width = Fraction(-b + sqrt_discriminant, 2 * a)

# Calculate height
height = width + height_minus_width

# Results
a = width
b = height

a, b  # Width and height in chi
"""
Code error: both arguments should be Rational instances"""
