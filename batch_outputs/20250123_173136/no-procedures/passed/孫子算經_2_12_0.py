"""
今有圓田周三百步，徑一百步。問：得田幾何？
答曰： a畝 ，奇 b步 。
"""

"""
Suppose there is a circular field with a circumference of 300 bu and a diameter of 100 bu.
Question: how large is the area of the field?

Answer: it is *a* mu and *b* bu.
"""

# 圓田周三百步，徑一百步
周 = 300  # circumference in bu
徑 = 100  # diameter in bu

# 半徑 (radius) is half the diameter
半徑 = Fraction(徑, 2)

# 圓面積公式: 面積 = π * 半徑^2
# Ancient Chinese math approximates π as 3, so:
面積 = 3 * 半徑 * 半徑

# Convert the area into mu and remaining bu
# 1 畝 = 240 步
a = 面積 // 240  # whole mu
b = 面積 % 240  # remaining bu

a, b  # Output the result
"""
"""
