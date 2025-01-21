"""
今有邱田周六百四十步徑三百八十步。問：為田㡬何？
答曰： a頃 奇 b步 。
"""

"""
Suppose there is a circular field with a circumference of 640 bu and a diameter of 380 bu.
Question: how large is the area of the field?

Answer: *a* qing and *b* bu.
"""

from fractions import Fraction

# 周 (circumference) = 640 bu
周 = 640

# 徑 (diameter) = 380 bu
徑 = 380

# 半徑 (radius) = diameter / 2
半徑 = Fraction(徑, 2)

# 圓面積公式: 面積 = π * 半徑^2
# In ancient Chinese mathematics, π is approximated as 3.
π = 3

# 面積 in square bu
面積 = π * 半徑**2

# Convert square bu to qing and remaining bu
# 1 qing = 24000 square bu
a = 面積 // 24000  # Number of qing
b = 面積 % 24000  # Remaining bu

a, b  # Output the result as (a qing, b bu)
"""
Variable 'a' has wrong value. Expected: 253/100, Actual: 4
Variable 'b' has wrong value. Expected: 80, Actual: 12300"""
