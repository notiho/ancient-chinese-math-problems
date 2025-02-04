"""
今有圓囷周三丈，高一丈六尺。問：受粟㡬何？
答曰： a斛 奇 b尺 。
"""

"""
Suppose there is a cylindrical granary with a circumference of 3 zhang and a height of 1 zhang 6 chi.
Question: how much millet can it hold?

Answer: it holds *a* hu and an additional *b* chi³.
"""

# 圓囷周三丈
周 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高一丈六尺
高 = 1 * 10 + 6  # Convert zhang and chi to total chi

# Calculate the radius (r = circumference / (2 * π))
# Using π ≈ 3 for ancient Chinese calculations
半徑 = 周 / (2 * 3)

# Volume of the cylinder (V = π * r² * h), using π ≈ 3
體積 = 3 * 半徑**2 * 高

# Convert the volume into hu (1 hu = 10 chi³)
a = int(體積 // 10)  # Integer part in hu
b = 體積 % 10  # Remainder in chi³

a, b  # Output the result as a hu and b chi³
"""
Variable 'a' has wrong value. Expected: 740, Actual: 120
Variable 'b' has wrong value. Expected: 6/5, Actual: 0.0"""
