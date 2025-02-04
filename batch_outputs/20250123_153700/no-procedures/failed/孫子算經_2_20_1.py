"""
今有邱田周六百三十九，步徑三百八十步。問：為田幾何？
答曰： a頃 。
"""

"""
Suppose there is a circular field with a circumference of 639 bu and a diameter of 380 bu.
Question: how large is the area of the field?

Answer: it is *a* qing.
"""

# 周 (circumference) = 639 bu
周 = 639

# 徑 (diameter) = 380 bu
徑 = 380

# Calculate the radius (半徑)
半徑 = Fraction(徑, 2)

# Area of a circle = π * r^2
# Ancient Chinese approximation for π is 3
π = 3
田積 = π * 半徑 * 半徑

# Convert the area from square bu to qing
# 1 qing = 24000 square bu
a = Fraction(田積, 24000)
"""
Variable 'a' has wrong value. Expected: 4047/1600, Actual: 361/80"""
