"""
今有環田外周三十步內周一十二步徑三步。問：為田㡬何？
答曰： a步 。
"""

"""
Suppose there is a circular field with an outer circumference of 30 bu, an inner circumference of 12 bu, and a width (diameter of the ring) of 3 bu.
Question: how much area does the field have?

Answer: *a* bu².
"""

# Import Fraction for precise calculations
from fractions import Fraction

# Outer circumference = 30 bu
外周 = 30

# Inner circumference = 12 bu
內周 = 12

# Diameter of the ring = 3 bu
徑 = 3

# Calculate the radius of the outer circle
外半徑 = Fraction(外周, 2 * 3)  # Circumference = 2πr, approximate π as 3

# Calculate the radius of the inner circle
內半徑 = Fraction(內周, 2 * 3)  # Circumference = 2πr, approximate π as 3

# Area of the outer circle = πr², approximate π as 3
外面積 = 3 * 外半徑**2

# Area of the inner circle = πr², approximate π as 3
內面積 = 3 * 內半徑**2

# Area of the ring-shaped field = Outer area - Inner area
a = 外面積 - 內面積

# Output the result
a
"""
"""
