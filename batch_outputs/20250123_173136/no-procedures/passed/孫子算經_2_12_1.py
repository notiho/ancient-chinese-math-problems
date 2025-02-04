"""
今有圓田周三百步，徑一百步。問：得田幾何？
答曰： a畝 ，奇 b步 。
"""

"""
Suppose there is a circular field with a circumference of 300 bu and a diameter of 100 bu.
Question: how much area does the field cover?

Answer: it covers *a* mu and *b* bu (remainder).
"""

# 圓田周三百步
周 = 300

# 徑一百步
徑 = 100

# 半徑 (radius) is half of the diameter
半徑 = Fraction(徑, 2)

# 圓面積公式：π * r^2
# Ancient Chinese approximation for π is 3
圓面積 = 3 * 半徑 * 半徑

# Convert the area into mu and remainder bu
# 1 畝 = 240 步
a = 圓面積 // 240  # Integer part in mu
b = 圓面積 % 240   # Remainder in bu

a, b  # Output the result
"""
"""
