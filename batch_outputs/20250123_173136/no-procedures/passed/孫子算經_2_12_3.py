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
周 = 300
徑 = 100

# 半徑 = 徑 / 2
半徑 = Fraction(徑, 2)

# 圓面積公式：面積 = π * 半徑^2
# 古代中國數學中，圓周率 π 通常取 3，因此：
π = 3
面積 = π * 半徑 * 半徑

# 1 畝 = 240 平方步
a = 面積 // 240  # 畝數
b = 面積 % 240   # 剩餘的平方步數

a, b
"""
"""
