"""
今有環田外周三十步內周一十二步徑三步。問：為田㡬何？
答曰： a步 。
"""

"""
Suppose there is a circular ring-shaped field. The outer circumference is 30 bu, and the inner circumference is 12 bu. The width of the ring (the difference between the outer and inner radii) is 3 bu.
Question: how much area does the field have?

Answer: *a* bu².
"""

# Importing Fraction to handle non-integer values
from fractions import Fraction

# Outer circumference
外周 = 30

# Inner circumference
內周 = 12

# Width of the ring (difference between outer and inner radii)
徑 = 3

# Calculate the outer radius (r_outer) using the formula for circumference: C = 2 * π * r
外半徑 = Fraction(外周, 2 * 3)  # π is approximated as 3 in ancient Chinese mathematics

# Calculate the inner radius (r_inner) using the same formula
內半徑 = Fraction(內周, 2 * 3)

# Calculate the area of the outer circle: A_outer = π * r_outer²
外面積 = 3 * 外半徑 * 外半徑

# Calculate the area of the inner circle: A_inner = π * r_inner²
內面積 = 3 * 內半徑 * 內半徑

# The area of the ring-shaped field is the difference between the outer and inner areas
a = 外面積 - 內面積

# Output the result
a
"""
"""
