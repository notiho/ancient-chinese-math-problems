"""
今有戶高多於廣六尺八寸，兩隅相去適一丈。問︰戶高、廣各幾何？
荅曰：廣 a尺 ；高 b尺 。
"""

#----- content starts here -----
"""
Suppose there is a door where the height exceeds the width by 6 chi and 8 cun (6.8 chi). The diagonal distance between the two opposite corners of the door is exactly 1 zhang (10 chi).
Question: what are the width and height of the door?

Answer: the width is *a* chi, and the height is *b* chi.
"""

# Importing Fraction to handle fractional values
from fractions import Fraction

# The diagonal distance (hypotenuse) of the door
diagonal = 10  # 1 zhang = 10 chi

# The height exceeds the width by 6 chi and 8 cun (6.8 chi)
difference = Fraction(68, 10)  # 6 chi 8 cun = 6.8 chi

# Let the width be x (in chi)
# Then the height is x + 6.8 (in chi)

# Using the Pythagorean theorem: width^2 + height^2 = diagonal^2
# x^2 + (x + 6.8)^2 = 10^2

# Expanding the equation:
# x^2 + (x^2 + 2 * x * 6.8 + 6.8^2) = 100
# 2 * x^2 + 13.6 * x + 46.24 = 100
# 2 * x^2 + 13.6 * x - 53.76 = 0

# Simplify the quadratic equation:
# x^2 + 6.8 * x - 26.88 = 0

# Solve the quadratic equation using the quadratic formula:
# x = (-b ± sqrt(b^2 - 4ac)) / 2a
# Here, a = 1, b = 6.8, c = -26.88

a = 1
b = Fraction(68, 10)  # 6.8
c = Fraction(-2688, 100)  # -26.88

# Calculate the discriminant: b^2 - 4ac
discriminant = b**2 - 4 * a * c

# Calculate the two possible solutions for x:
x1 = (-b + discriminant**0.5) / (2 * a)
x2 = (-b - discriminant**0.5) / (2 * a)

# Since width must be positive, we choose the positive solution:
width = x1 if x1 > 0 else x2

# Calculate the height:
height = width + difference

# Final results:
a = width  # Width of the door
b = height  # Height of the door

# Output the results
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 14/5, Actual: 2.8000000000000003
Variable 'b' has wrong value. Expected: 48/5, Actual: 9.6"""
