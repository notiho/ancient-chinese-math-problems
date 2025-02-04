"""
今有圓田，周三十步，徑十步。問：為田幾何？
荅曰： a步 。
"""

"""
Suppose there is a circular field with a circumference of 30 bu and a diameter of 10 bu.
Question: how large is the area of the field?

Answer: the area is *a* square bu.
"""

# 圓田公式: 面積 = (徑 * 徑) * 3 / 4

# 徑十步
徑 = 10

# 計算面積
a = Fraction(徑 * 徑 * 3, 4)  # Using the ancient Chinese approximation of π as 3
"""
"""
