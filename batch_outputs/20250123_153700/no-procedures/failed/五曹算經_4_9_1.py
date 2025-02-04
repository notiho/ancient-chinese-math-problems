"""
今有內角聚粟下周五十四尺高五尺。問：粟㡬何？
答曰： a斛 。
"""

"""
Suppose there is a granary with a circular base. The circumference of the base is 54 chi, and the height is 5 chi.
Question: how much millet can it hold?

Answer: it holds *a* hu.
"""

# 周 = 54尺 (circumference of the base)
周 = 54

# 高 = 5尺 (height)
高 = 5

# The formula for the volume of a cylinder is: V = (周 / 2π)^2 * π * 高
# Simplifying, V = (周^2 * 高) / (4π)
# In ancient Chinese math, π is approximated as 3.

# Approximation of π
π = 3

# Calculate the radius squared
radius_squared = (周 / (2 * π)) ** 2

# Calculate the volume of the granary
volume = radius_squared * π * 高

# Convert the volume from cubic chi to hu (1 hu = 10 cubic chi)
a = Fraction(volume, 10)
"""
Code error: both arguments should be Rational instances"""
