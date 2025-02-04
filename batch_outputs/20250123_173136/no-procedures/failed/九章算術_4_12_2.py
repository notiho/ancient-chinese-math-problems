"""
又有積二萬五千二百八十一步。問︰為方幾何？
荅曰： a步 。
"""

"""
Suppose there is a volume of 25,281 cubic bu (步).
Question: what is the side length of the cube?

Answer: the side length is *a* bu.
"""

# 積二萬五千二百八十一步
volume = 25281

# To find the side length of a cube, take the cube root of the volume.
# Since we are working with exact fractions, we will find the cube root manually.

# Start with an approximation and refine it:
# a^3 = volume
# a = volume^(1/3)

# Manually solving for the cube root:
# 29^3 = 24389
# 30^3 = 27000
# Therefore, the cube root lies between 29 and 30.

# Exact solution:
a = 29  # Since 29^3 = 24389, which is the closest integer cube root.
"""
Variable 'a' has wrong value. Expected: 159, Actual: 29"""
