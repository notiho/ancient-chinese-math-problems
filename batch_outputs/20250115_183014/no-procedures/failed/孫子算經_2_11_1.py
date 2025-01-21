"""
今有圓窖，周五丈四尺，深一丈八尺。問：受粟幾何？
答曰： a斛 。
"""

"""
Suppose there is a circular pit with a circumference of 5 zhang and 4 chi, and a depth of 1 zhang and 8 chi.
Question: how much millet can it hold?

Answer: it holds *a* hu.
"""

# 周五丈四尺 (circumference = 5 zhang 4 chi)
周 = 5 * 10 + 4  # Convert zhang to chi (1 zhang = 10 chi)

# 深一丈八尺 (depth = 1 zhang 8 chi)
深 = 1 * 10 + 8  # Convert zhang to chi

# Calculate the radius of the circular pit
# Circumference = 2 * π * radius
# Using π = 3, radius = 周 / (2 * π)
半徑 = Fraction(周, 2 * 3)

# Volume of the circular pit = π * r^2 * depth
# Using π = 3
體積 = 3 * 半徑**2 * 深

# Convert chi^3 to hu (1 hu = 10 chi^3)
a = Fraction(體積, 10)  # Convert volume to hu

a  # Output the result
"""
Variable 'a' has wrong value. Expected: 2700, Actual: 2187/5"""
