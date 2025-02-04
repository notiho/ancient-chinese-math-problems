"""
今有圓田周七十八步徑二十六步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a circular field with a circumference of 78 bu and a diameter of 26 bu.
Question: how large is the area of the field?

Answer: it is *a* mu and *b* bu².
"""

# 圓田周 (circumference) = 78 步
周 = 78

# 圓田徑 (diameter) = 26 步
徑 = 26

# 半徑 (radius) = diameter / 2
半徑 = Fraction(徑, 2)

# 圓面積公式: 面積 = π * 半徑²
# Ancient Chinese approximation for π = 3
π = 3

# Calculate the area in bu²
面積 = π * 半徑 * 半徑

# Convert the area into mu and remaining bu²
# 1 畝 = 240 步²
a = 面積 // 240  # Whole mu
b = 面積 % 240   # Remaining bu²

a, b  # Output the result as (a mu, b bu²)
"""
"""
