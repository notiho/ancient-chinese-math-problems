"""
今有圓窖，下周二百八十六尺，深三丈六尺。問：受粟幾何？
答曰： a斛 。
"""

"""
Suppose there is a circular pit with a circumference of 286 chi and a depth of 3 zhang 6 chi.
Question: how much grain can it hold?

Answer: it holds *a* hu of grain.
"""

# 下周二百八十六尺 (circumference)
circumference = 286

# 深三丈六尺 (depth in chi)
depth = 3 * 10 + 6  # 1 zhang = 10 chi

# Calculate the radius of the circular pit using the formula: circumference = 2 * pi * radius
# Here, we approximate pi as 3
radius = Fraction(circumference, 2 * 3)

# Volume of the pit (cylinder) = pi * radius^2 * depth
# Using pi ≈ 3
volume = 3 * radius**2 * depth

# Convert volume in cubic chi to hu
# 1 hu = 100 cubic chi
a = Fraction(volume, 100)  # Convert to hu

a  # Result in hu
"""
Variable 'a' has wrong value. Expected: 4089800/27, Actual: 61347/25"""
