"""
今有邱田周六百四十步徑三百八十步。問：為田㡬何？
答曰： a頃 奇 b步 。
"""

"""
Suppose there is a circular field with a circumference of 640 bu and a diameter of 380 bu.
Question: how large is the area of the field?

Answer: it is *a* qing and *b* bu.
"""

# 周 (circumference) = 640 bu
周 = 640

# 徑 (diameter) = 380 bu
徑 = 380

# Calculate the radius (半徑)
半徑 = Fraction(徑, 2)

# Area of a circle = π * r^2
# In ancient Chinese mathematics, π is approximated as 3.
面積 = 3 * 半徑 * 半徑

# Convert the area into qing and bu
# 1 qing = 24000 bu^2
a = 面積 // 24000  # Integer part (qing)
b = 面積 % 24000   # Remainder (bu)

# The result is `a` qing and `b` bu.
"""
Variable 'a' has wrong value. Expected: 253/100, Actual: 4
Variable 'b' has wrong value. Expected: 80, Actual: 12300"""
