"""
今有圓田，周三十步，徑十步。問：為田幾何？
荅曰： a步 。
"""

"""
Suppose there is a circular field with a circumference of 30 bu and a diameter of 10 bu.
Question: how large is the area of the field?

Answer: it is *a* bu².
"""

# 周三十步
周 = 30

# 徑十步
徑 = 10

# 半徑 = 徑 / 2
半徑 = Fraction(徑, 2)

# 圓面積公式: π * r²
# In ancient Chinese mathematics, π is approximated as 3.
π = 3

# 面積 = π * 半徑²
a = π * 半徑 * 半徑

a  # The area of the circular field in bu²
"""
"""
