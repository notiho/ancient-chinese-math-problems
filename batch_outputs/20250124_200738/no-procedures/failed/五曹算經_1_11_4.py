"""
今有邱田周六百四十步徑三百八十步。問：為田㡬何？
答曰： a頃 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a circular field with a circumference of 640 bu and a diameter of 380 bu.
Question: how large is the area of the field?

Answer: *a* qing and *b* bu.
"""

# 周 (circumference) = 640 bu
周 = 640

# 徑 (diameter) = 380 bu
徑 = 380

# 半徑 (radius) = 徑 / 2
半徑 = Fraction(徑, 2)

# 圓面積公式: 面積 = π * 半徑^2
# Ancient Chinese approximation for π = 3
π = 3

# Calculate area in square bu
面積 = π * 半徑 * 半徑

# Convert square bu to qing and remaining bu
# 1 qing = 24000 square bu
a = 面積 // 24000  # Integer part in qing
b = 面積 % 24000   # Remainder in square bu

a, b  # Output the result in qing and bu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 253/100, Actual: 4
Variable 'b' has wrong value. Expected: 80, Actual: 12300"""
