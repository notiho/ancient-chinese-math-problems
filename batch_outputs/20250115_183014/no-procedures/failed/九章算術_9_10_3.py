"""
今有戶高多於廣六尺八寸，兩隅相去適一丈。問︰戶高、廣各幾何？
荅曰：廣 a尺 ；高 b尺 。
"""

"""
Suppose there is a door where the height exceeds the width by 6 chi and 8 cun (6.8 chi). The diagonal distance between the two opposite corners is exactly 1 zhang (10 chi).
Question: what are the width and height of the door?

Answer: the width is *a* chi, and the height is *b* chi.
"""

# Define the relationship between height and width
# 高 = 廣 + 6.8
height_minus_width = Fraction(68, 10)  # 6 chi 8 cun = 6.8 chi

# The diagonal distance is given by the Pythagorean theorem
# diagonal^2 = width^2 + height^2
# 10^2 = 廣^2 + (廣 + 6.8)^2

diagonal = 10  # 1 zhang = 10 chi

# Solve for width (廣)
from fractions import Fraction

# Expand the equation:
# 10^2 = 廣^2 + (廣 + 6.8)^2
# 100 = 廣^2 + 廣^2 + 2 * 廣 * 6.8 + 6.8^2
# 100 = 2 * 廣^2 + 13.6 * 廣 + 46.24

# Rearrange into standard quadratic form:
# 2 * 廣^2 + 13.6 * 廣 - 53.76 = 0

# Divide through by 2 to simplify:
# 廣^2 + 6.8 * 廣 - 26.88 = 0

# Use the quadratic formula to solve for 廣:
# 廣 = (-b ± sqrt(b^2 - 4ac)) / 2a
# Here, a = 1, b = 6.8, c = -26.88

a_coeff = 1
b_coeff = Fraction(68, 10)  # 6.8
c_coeff = Fraction(-2688, 100)  # -26.88

# Calculate the discriminant:
discriminant = b_coeff**2 - 4 * a_coeff * c_coeff

# Calculate the two possible solutions for 廣:
width_1 = (-b_coeff + discriminant**0.5) / (2 * a_coeff)
width_2 = (-b_coeff - discriminant**0.5) / (2 * a_coeff)

# Since width must be positive, choose the positive solution:
a = width_1 if width_1 > 0 else width_2

# Calculate the height (高):
b = a + height_minus_width

# Output the results:
a, b  # Width (廣) and Height (高) in chi
"""
Variable 'a' has wrong value. Expected: 14/5, Actual: 2.8000000000000003
Variable 'b' has wrong value. Expected: 48/5, Actual: 9.6"""
