"""
今有外角聚粟下周四十八尺高六尺。問：粟㡬何？
答曰： a斛 奇 b分 。
"""

"""
Suppose there is a granary in the shape of a cone with a base circumference of 48 chi and a height of 6 chi.
Question: how much millet can it hold?

Answer: *a* hu and *b* fen.
"""

# Base circumference (周) = 48 chi
周 = 48

# Height (高) = 6 chi
高 = 6

# To calculate the volume of a cone, we need the radius of the base.
# Circumference = 2 * pi * radius
# Radius = 周 / (2 * pi)
# Using an approximation of pi = 3 for simplicity (as was often done in ancient Chinese calculations):
pi = 3
半徑 = 周 / (2 * pi)

# Volume of the cone = (1/3) * pi * r^2 * h
體積 = Fraction(1, 3) * pi * 半徑**2 * 高

# 1 hu = 10 chi^3, so convert the volume from chi^3 to hu
a = 體積 // 10  # Integer part (hu)
b = 體積 % 10  # Remainder (fen)

a, b
"""
Variable 'a' has wrong value. Expected: 316, Actual: 38.0
Variable 'b' has wrong value. Expected: 8, Actual: 4.0"""
