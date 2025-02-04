"""
今有圓窖，周五丈四尺，深一丈八尺。問：受粟幾何？
答曰： a斛 。
"""

"""
Suppose there is a circular pit with a circumference of 5 zhang 4 chi and a depth of 1 zhang 8 chi.
Question: how much millet can it hold?

Answer: it holds *a* hu.
"""

# 周五丈四尺
周 = 5 * 10 + 4  # Convert zhang to chi (1 zhang = 10 chi)

# 深一丈八尺
深 = 1 * 10 + 8  # Convert zhang to chi

# Calculate the radius of the circular pit
# Circumference = 2 * pi * radius
# Using pi = 3, radius = 周 / (2 * pi) = 周 / 6
半徑 = Fraction(周, 6)

# Volume of the pit (cylinder) = pi * r^2 * depth
# Using pi = 3, volume = 3 * 半徑^2 * 深
體積 = 3 * 半徑**2 * 深

# Convert the volume from cubic chi to hu
# 1 hu = 10 cubic chi
a = Fraction(體積, 10)  # Convert to hu
"""
Variable 'a' has wrong value. Expected: 2700, Actual: 2187/5"""
