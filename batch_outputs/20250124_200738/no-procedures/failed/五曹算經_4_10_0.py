"""
今有半壁聚粟下周三十六尺高四尺五寸。問：粟㡬何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is a half-wall (semi-cylindrical) granary filled with millet. The circumference at the base is 36 chi, and the height is 4 chi and 5 cun.
Question: how much millet does it hold?

Answer: it holds *a* hu.
"""

# Import Fraction for precise calculations
from fractions import Fraction

# 半壁聚粟 (semi-cylindrical granary)
# 下周三十六尺 (circumference at the base is 36 chi)
circumference = 36

# 高四尺五寸 (height is 4 chi and 5 cun)
height = 4 + Fraction(5, 10)  # Convert 5 cun to chi (1 chi = 10 cun)

# 半徑 = 周長 / (2 * π)
# Using π ≈ 3 for ancient Chinese calculations
radius = Fraction(circumference, 2 * 3)

# 半圓面積 = (1/2) * π * r^2
# Using π ≈ 3
semi_circle_area = Fraction(1, 2) * 3 * radius**2

# 體積 = 半圓面積 * 高
volume = semi_circle_area * height

# 1 cubic chi = 1 hu (ancient Chinese unit conversion)
a = volume  # The volume in cubic chi is directly the amount of millet in hu

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 200, Actual: 243"""
