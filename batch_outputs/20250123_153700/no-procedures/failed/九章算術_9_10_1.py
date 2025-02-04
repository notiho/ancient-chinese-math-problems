"""
今有戶高多於廣六尺八寸，兩隅相去適一丈。問︰戶高、廣各幾何？
荅曰：廣 a尺 ；高 b尺 。
"""

"""
Suppose there is a door where the height exceeds the width by 6 chi and 8 cun (6.8 chi). The diagonal distance between the two opposite corners of the door is exactly 1 zhang (10 chi).
Question: What are the width and height of the door?

Answer: The width is *a* chi, and the height is *b* chi.
"""

# Using the Pythagorean theorem: diagonal^2 = width^2 + height^2
# Let the width be x (in chi), and the height be x + 6.8 (in chi).
# The diagonal is 10 chi.

from fractions import Fraction

# Diagonal
diagonal = 10

# Difference between height and width
difference = Fraction(68, 10)  # 6 chi 8 cun = 6.8 chi

# Solve for width (x) using the Pythagorean theorem:
# (width)^2 + (width + difference)^2 = diagonal^2
# x^2 + (x + 6.8)^2 = 10^2
# x^2 + x^2 + 13.6x + 46.24 = 100
# 2x^2 + 13.6x - 53.76 = 0

# Coefficients of the quadratic equation
a_coeff = 2
b_coeff = Fraction(136, 10)  # 13.6
c_coeff = Fraction(-5376, 100)  # -53.76

# Solve the quadratic equation using the quadratic formula:
# x = (-b ± sqrt(b^2 - 4ac)) / 2a

# Calculate discriminant
discriminant = b_coeff**2 - 4 * a_coeff * c_coeff

# Calculate the two possible solutions for width
width1 = (-b_coeff + discriminant**0.5) / (2 * a_coeff)
width2 = (-b_coeff - discriminant**0.5) / (2 * a_coeff)

# Since width must be positive, choose the positive solution
a = width1 if width1 > 0 else width2

# Calculate height
b = a + difference

# Output the results
a, b  # Width (a) and height (b) in chi
"""
Variable 'a' has wrong value. Expected: 14/5, Actual: 2.8000000000000003
Variable 'b' has wrong value. Expected: 48/5, Actual: 9.6"""
