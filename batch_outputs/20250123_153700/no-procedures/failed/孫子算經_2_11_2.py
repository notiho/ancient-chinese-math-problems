"""
今有圓窖，周五丈四尺，深一丈八尺。問：受粟幾何？
答曰： a斛 。
"""

"""
Suppose there is a circular silo with a circumference of 5 zhang and 4 chi, and a depth of 1 zhang and 8 chi.
Question: how much millet can it hold?

Answer: it holds *a* hu.
"""

# 周五丈四尺
周 = 5 * 10 + 4  # Convert zhang and chi to chi (1 zhang = 10 chi)

# 深一丈八尺
深 = 1 * 10 + 8  # Convert zhang and chi to chi

# Calculate the radius of the circular base
# Circumference = 2 * pi * radius
# Using pi = 3 (as was common in ancient Chinese mathematics)
半徑 = Fraction(周, 2 * 3)

# Calculate the area of the circular base
# Area = pi * radius^2
底面積 = 3 * 半徑 * 半徑

# Calculate the volume of the silo
# Volume = base area * depth
體積 = 底面積 * 深

# Convert volume from cubic chi to hu
# 1 hu = 10 cubic chi
a = Fraction(體積, 10)  # Convert cubic chi to hu

a  # The result in hu
"""
Variable 'a' has wrong value. Expected: 2700, Actual: 2187/5"""
