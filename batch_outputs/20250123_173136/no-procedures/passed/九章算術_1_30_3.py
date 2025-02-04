"""
今有圓田，周三十步，徑十步。問：為田幾何？
荅曰： a步 。
"""

"""
Suppose there is a circular field with a circumference of 30 bu and a diameter of 10 bu.
Question: how large is the area of the field?

Answer: the area is *a* bu².
"""

# 圓田公式：田 = (徑 × 徑) × 3 / 4

# 徑十步
徑 = 10

# 計算田的面積
a = Fraction(徑 * 徑 * 3, 4)  # Area of the circular field in bu²

a
"""
"""
