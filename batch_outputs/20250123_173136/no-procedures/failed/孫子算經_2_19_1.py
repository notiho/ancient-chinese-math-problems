"""
今有積，三萬五千步。問為圓幾何？
答曰： a步 。
"""

"""
Suppose there is a square area of 35,000 bu. 
Question: if this area is transformed into a circle, what is the diameter of the circle?

Answer: the diameter is *a* bu.
"""

# Square area
積 = 35000

# Formula for converting square area to a circle's diameter:
# Diameter = sqrt(4 * Area / π)
# In ancient Chinese mathematics, π was often approximated as 3.

# Using π = 3, the formula simplifies to:
# Diameter = sqrt(4 * Area / 3)

# Calculate the diameter
a = Fraction(4 * 積, 3) ** Fraction(1, 2)  # Square root of (4 * Area / 3)
"""
Variable 'a' has wrong value. Expected: 17498/27, Actual: 216.02468994692867"""
