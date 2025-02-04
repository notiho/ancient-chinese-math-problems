"""
今有半壁聚粟下周三十六尺高四尺五寸。問：粟㡬何？
答曰： a斛 。
"""

"""
Suppose there is a half-wall (semicircular) granary filled with millet. The base circumference is 36 chi, and the height is 4 chi and 5 cun.
Question: how much millet does it hold?

Answer: it holds *a* hu of millet.
"""

from fractions import Fraction

# 半壁聚粟下周三十六尺
circumference = 36  # chi

# 高四尺五寸
height = 4 + Fraction(5, 10)  # 4 chi and 5 cun (convert cun to chi)

# 半壁 (semicircular granary) volume formula: V = (1/2) * π * r^2 * h
# Circumference = 2 * π * r, so r = circumference / (2 * π)
# For simplicity, use π ≈ 3

pi = 3
radius = Fraction(circumference, 2 * pi)

# Volume of the granary
volume = Fraction(1, 2) * pi * radius**2 * height

# Convert volume from cubic chi to hu
# 1 hu = 10 cubic chi
a = volume / 10

a
"""
Variable 'a' has wrong value. Expected: 200, Actual: 243/10"""
