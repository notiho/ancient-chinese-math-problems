"""
今有戶高多於廣六尺八寸，兩隅相去適一丈。問︰戶高、廣各幾何？
荅曰：廣 a尺 ；高 b尺 。
"""

"""
Suppose there is a door where the height exceeds the width by 6 chi and 8 cun (6.8 chi). The diagonal distance between the two opposite corners of the door is exactly 1 zhang (10 chi).
Question: what are the width and height of the door?

Answer: the width is *a* chi, and the height is *b* chi.
"""

# Importing Fraction to handle fractional values
from fractions import Fraction

# The diagonal distance (hypotenuse) is 10 chi
diagonal = 10

# The height exceeds the width by 6.8 chi
difference = Fraction(68, 10)  # 6 chi 8 cun = 6.8 chi

# Let the width be x (in chi)
# Then the height is x + 6.8
# Using the Pythagorean theorem: width^2 + height^2 = diagonal^2
# x^2 + (x + 6.8)^2 = 10^2

# Solving the equation:
# x^2 + (x^2 + 13.6x + 46.24) = 100
# 2x^2 + 13.6x - 53.76 = 0

# Coefficients of the quadratic equation
a_coeff = 2
b_coeff = Fraction(136, 10)  # 13.6
c_coeff = Fraction(-5376, 100)  # -53.76

# Solving the quadratic equation using the quadratic formula:
# x = (-b ± sqrt(b^2 - 4ac)) / 2a

# Calculate the discriminant
discriminant = b_coeff**2 - 4 * a_coeff * c_coeff

# Calculate the two possible solutions for x
x1 = (-b_coeff + discriminant**0.5) / (2 * a_coeff)
x2 = (-b_coeff - discriminant**0.5) / (2 * a_coeff)

# Since width must be positive, we take the positive solution
width = x1 if x1 > 0 else x2

# Calculate the height
height = width + difference

# Final answers
a = width
b = height

# Output the results
a, b
"""
Variable 'a' has wrong value. Expected: 14/5, Actual: 2.8000000000000003
Variable 'b' has wrong value. Expected: 48/5, Actual: 9.6"""
