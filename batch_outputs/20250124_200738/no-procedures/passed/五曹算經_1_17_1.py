"""
今有環田外周三十步內周一十二步徑三步。問：為田㡬何？
答曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a circular field with an outer circumference of 30 bu, an inner circumference of 12 bu, and a width (diameter of the ring) of 3 bu.
Question: how much is the area of the field?

Answer: *a* bu².
"""

# Import Fraction for precise calculations
from fractions import Fraction

# Given data
外周 = 30  # Outer circumference in bu
內周 = 12  # Inner circumference in bu
徑 = 3     # Width (diameter of the ring) in bu

# Calculate the radii
外半徑 = Fraction(外周, 2 * 3)  # Outer radius = circumference / (2 * π), approximating π as 3
內半徑 = Fraction(內周, 2 * 3)  # Inner radius = circumference / (2 * π)

# Calculate the area of the outer circle and inner circle
外面積 = 3 * 外半徑**2  # Area of outer circle = π * r², approximating π as 3
內面積 = 3 * 內半徑**2  # Area of inner circle = π * r², approximating π as 3

# Calculate the area of the ring-shaped field
a = 外面積 - 內面積  # Area of the field = outer area - inner area

# Output the result
a#----- content ends here -----

"""
"""
