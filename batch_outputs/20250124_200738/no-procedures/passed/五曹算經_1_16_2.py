"""
今有圓田周七十八步徑二十六步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a circular field with a circumference of 78 bu and a diameter of 26 bu.
Question: how large is the area of the field?

Answer: *a* mu and *b* bu².
"""

# 圓田周 78 步
周 = 78

# 圓田徑 26 步
徑 = 26

# 半徑 (徑 / 2)
半徑 = Fraction(徑, 2)

# 圓面積公式: π * r^2
# Ancient Chinese approximation for π is 3 (used in early Chinese mathematics)
圓面積 = 3 * 半徑 * 半徑

# Convert the area into mu and bu²
# 1 畝 = 240 步²
a = 圓面積 // 240  # Integer part (mu)
b = 圓面積 % 240   # Remainder (bu²)

a, b  # Output the result as (a 畝, b 步²)#----- content ends here -----

"""
"""
