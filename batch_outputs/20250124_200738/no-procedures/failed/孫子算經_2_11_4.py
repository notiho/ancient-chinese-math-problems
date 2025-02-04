"""
今有圓窖，周五丈四尺，深一丈八尺。問：受粟幾何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is a circular pit with a circumference of 5 zhang 4 chi and a depth of 1 zhang 8 chi.
Question: how much millet can it hold?

Answer: it holds *a* hu.
"""

# 周五丈四尺 (circumference)
周 = 5 * 10 + 4  # Convert zhang to chi (1 zhang = 10 chi)

# 深一丈八尺 (depth)
深 = 1 * 10 + 8  # Convert zhang to chi

# Calculate the radius using the formula: 周 = 2 * pi * r
# Approximate pi as 3 for ancient Chinese calculations
pi = 3
半徑 = Fraction(周, 2 * pi)

# Volume of the pit (cylinder): V = pi * r^2 * h
體積 = pi * 半徑**2 * 深

# Convert the volume from cubic chi to hu
# 1 hu = 10 cubic chi
a = Fraction(體積, 10)

# Result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2700, Actual: 2187/5"""
