"""
今有邱田周六百四十步徑三百八十步。問：為田㡬何？
答曰： a頃 奇 b步 。
"""

"""
Suppose there is a circular field with a circumference of 640 bu and a diameter of 380 bu.
Question: how large is the area of the field?

Answer: *a* qing and *b* bu.
"""

# 周 = 640步
周 = 640

# 徑 = 380步
徑 = 380

# 半徑 = 徑 / 2
半徑 = Fraction(徑, 2)

# 圓面積公式: 面積 = π * 半徑^2
# Ancient Chinese math approximates π as 3, so:
面積 = 3 * 半徑 * 半徑

# Convert the area into qing and bu
# 1 qing = 24000 bu²
a = 面積 // 24000  # 整數部分為頃數
b = 面積 % 24000   # 餘數部分為步數

a, b  # Output the result as (a qing, b bu)
"""
Variable 'a' has wrong value. Expected: 253/100, Actual: 4
Variable 'b' has wrong value. Expected: 80, Actual: 12300"""
