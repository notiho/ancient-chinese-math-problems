"""
今有半壁聚粟下周三十六尺高四尺五寸。問：粟㡬何？
答曰： a斛 。
"""

"""
Suppose there is a half-wall (semi-cylindrical) granary filled with millet. The circumference at the base is 36 chi, and the height is 4 chi and 5 cun.
Question: how much millet does it contain?

Answer: it contains *a* hu.
"""

# Import Fraction for precise calculations
from fractions import Fraction

# 半壁聚粟 (semi-cylindrical granary)
# 下周三十六尺 (circumference at the base is 36 chi)
circumference = 36

# 高四尺五寸 (height is 4 chi and 5 cun)
height = 4 + Fraction(5, 10)  # Convert 5 cun to chi (1 chi = 10 cun)

# 半徑 = 周長 / (2 * π)
# Since π ≈ 3, we approximate the radius as:
radius = Fraction(circumference, 2 * 3)

# 半圓柱體積公式: V = (1/2) * π * r^2 * h
# Using π ≈ 3, the volume becomes:
volume = Fraction(1, 2) * 3 * radius**2 * height

# 1 cubic chi = 10 dou = 1 hu
# Convert cubic chi to hu:
a = Fraction(volume, 10)

# Final result
a
"""
Variable 'a' has wrong value. Expected: 200, Actual: 243/10"""
