"""
今有圓囷周三丈，高一丈六尺。問：受粟㡬何？
答曰： a斛 奇 b尺 。
"""

#----- content starts here -----
"""
Suppose there is a cylindrical granary with a circumference of 3 zhang and a height of 1 zhang 6 chi.
Question: how much grain can it hold?

Answer: it holds *a* hu and an additional *b* chi³.
"""

# 圓囷周三丈
周 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高一丈六尺
高 = 1 * 10 + 6  # Convert zhang and chi to chi

# 圓的直徑 = 周 / π (using π ≈ 3 for ancient Chinese calculations)
直徑 = Fraction(周, 3)

# 圓的半徑 = 直徑 / 2
半徑 = Fraction(直徑, 2)

# 圓的面積 = π * 半徑² (using π ≈ 3)
面積 = 3 * 半徑 * 半徑

# 圓柱體積 = 面積 * 高
體積 = 面積 * 高

# 1 hu = 10 chi³, so convert the volume to hu and remaining chi³
a = 體積 // 10  # Integer part in hu
b = 體積 % 10  # Remainder in chi³#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 740, Actual: 120
Variable 'b' has wrong value. Expected: 6/5, Actual: 0"""
