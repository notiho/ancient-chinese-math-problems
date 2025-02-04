"""
今有池方一丈，葭生其中央，出水一尺。引葭赴岸，適與岸齊。問︰水深、葭長各幾何？
荅曰：水深 a丈 ；葭長 b丈 。
"""

#----- content starts here -----
"""
Suppose there is a square pond with a side length of 1 zhang. A reed grows at the center of the pond and extends 1 chi above the water surface. 
When the reed is bent toward the edge of the pond, it just reaches the edge.

Question: How deep is the water, and how long is the reed?

Answer: The water depth is *a* zhang, and the reed length is *b* zhang.
"""

# Import Fraction for precise calculations
from fractions import Fraction

# Given values
pond_side = Fraction(1)  # 1 zhang (side length of the pond)
reed_above_water = Fraction(1, 10)  # 1 chi = 1/10 zhang

# Let the water depth be `x` (in zhang)
# The reed length is the water depth plus the part above water: `reed_length = x + reed_above_water`
# Using the Pythagorean theorem:
# (reed_length)^2 = (pond_side / 2)^2 + (water_depth)^2
# (x + 1/10)^2 = (1/2)^2 + x^2

# Solve step by step:
# Expand (x + 1/10)^2
# x^2 + 2 * x * (1/10) + (1/10)^2 = (1/2)^2 + x^2
# x^2 + 2x/10 + 1/100 = 1/4 + x^2
# Cancel x^2 from both sides:
# 2x/10 + 1/100 = 1/4
# Simplify:
# x/5 + 1/100 = 25/100
# x/5 = 24/100
# x = (24/100) * 5
# x = 120/100 = 6/5

# Water depth (a):
a = Fraction(6, 5)  # 6/5 zhang

# Reed length (b):
b = a + reed_above_water  # x + 1/10
b = Fraction(6, 5) + Fraction(1, 10)
b = Fraction(12, 10) + Fraction(1, 10)
b = Fraction(13, 10)  # 13/10 zhang

# Final results
print(f"Water depth (a): {a} zhang")
print(f"Reed length (b): {b} zhang")#----- content ends here -----

"""
"""
