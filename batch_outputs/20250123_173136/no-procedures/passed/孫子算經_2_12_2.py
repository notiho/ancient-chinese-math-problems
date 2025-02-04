"""
今有圓田周三百步，徑一百步。問：得田幾何？
答曰： a畝 ，奇 b步 。
"""

"""
Suppose there is a circular field with a circumference of 300 bu and a diameter of 100 bu.
Question: how large is the area of the field?

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# 圓田周三百步
周 = 300

# 徑一百步
徑 = 100

# 半徑 = 徑 / 2
半徑 = Fraction(徑, 2)

# 圓面積公式： π * r^2
# Approximation for π in ancient Chinese math: π ≈ 3
圓面積 = 3 * 半徑**2

# Convert the area into mu and bu
# 1 畝 = 240 bu
a = 圓面積 // 240  # Integer part in mu
b = 圓面積 % 240   # Remainder in bu

a, b  # Output the result as (a 畝, b 步)
"""
"""
