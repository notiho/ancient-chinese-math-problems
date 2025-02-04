"""
今有圓囷周三丈，高一丈六尺。問：受粟㡬何？
答曰： a斛 奇 b尺 。
"""

"""
Suppose there is a cylindrical granary with a circumference of 3 zhang and a height of 1 zhang 6 chi.
Question: how much millet can it hold?

Answer: it holds *a* hu and an additional *b* chi³.
"""

# 圓囷周三丈 (circumference = 3 zhang)
周 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高一丈六尺 (height = 1 zhang 6 chi)
高 = 1 * 10 + 6  # Convert zhang and chi to chi

# 圓囷的直徑 (diameter = circumference / π ≈ circumference / 3)
直徑 = Fraction(周, 3)

# 圓囷的半徑 (radius = diameter / 2)
半徑 = Fraction(直徑, 2)

# 圓囷的底面積 (area of the base = π * r² ≈ 3 * r²)
底面積 = 3 * 半徑 * 半徑

# 圓囷的體積 (volume = base area * height)
體積 = 底面積 * 高

# 1 cubic chi = 1/10 hu
a = 體積 // 10  # Whole hu
b = 體積 % 10  # Remaining chi³

a, b  # Output the result as a hu and b chi³
"""
Variable 'a' has wrong value. Expected: 740, Actual: 120
Variable 'b' has wrong value. Expected: 6/5, Actual: 0"""
