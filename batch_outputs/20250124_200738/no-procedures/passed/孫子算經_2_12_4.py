"""
今有圓田周三百步，徑一百步。問：得田幾何？
答曰： a畝 ，奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a circular field with a circumference of 300 bu and a diameter of 100 bu.
Question: how large is the area of the field?

Answer: *a* mu, with a remainder of *b* bu.
"""

# 圓田周三百步
周 = 300

# 徑一百步
徑 = 100

# 半徑
半徑 = Fraction(徑, 2)

# 圓面積公式：π * r^2
# Ancient Chinese approximation for π is 3.
圓面積 = 3 * 半徑 * 半徑

# Convert the area into mu (1 mu = 240 bu^2)
a = 圓面積 // 240  # Whole mu
b = 圓面積 % 240   # Remaining bu^2

a, b  # Output the result#----- content ends here -----

"""
"""
