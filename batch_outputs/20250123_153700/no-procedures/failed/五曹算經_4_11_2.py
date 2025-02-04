"""
今有外角聚粟下周四十八尺高六尺。問：粟㡬何？
答曰： a斛 奇 b分 。
"""

"""
Suppose there is a granary shaped like a cone. The circumference of the base is 48 chi, and the height is 6 chi.
Question: how much millet can it hold?

Answer: *a* hu and *b* fen.
"""

# Import Fraction for precise calculations
from fractions import Fraction

# Given values
周 = 48  # circumference of the base in chi
高 = 6   # height in chi

# Step 1: Calculate the radius of the base
# Circumference = 2 * pi * radius
# Radius = 周 / (2 * pi)
# Using an approximation of pi = 3 for ancient Chinese calculations
半徑 = Fraction(周, 6)

# Step 2: Calculate the volume of the cone
# Volume of a cone = (1/3) * pi * r^2 * h
# Using pi = 3
體積 = Fraction(1, 3) * 3 * 半徑**2 * 高

# Step 3: Convert the volume into hu and fen
# 1 hu = 10 chi^3
a = 體積 // 10  # Integer part in hu
b = 體積 % 10   # Remainder in fen

a, b  # Output the result as hu and fen
"""
Variable 'a' has wrong value. Expected: 316, Actual: 38
Variable 'b' has wrong value. Expected: 8, Actual: 4"""
