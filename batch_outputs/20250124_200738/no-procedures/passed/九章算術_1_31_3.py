"""
又有圓田，周一百八十一步，徑六十步三分步之一。問：為田幾何？
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is a circular field with a circumference of 181 bu and a diameter of 60 + 1/3 bu.
Question: how large is the area of the field?

Answer: *a* mu.
"""

from fractions import Fraction

# 周 = 181步
周 = 181

# 徑 = 60步 + 1/3步
徑 = 60 + Fraction(1, 3)

# 半徑 = 徑 / 2
半徑 = 徑 / 2

# 圓面積公式：面積 = π * 半徑^2
# 古代中國用 π ≈ 3
π = 3

# 面積 (以平方步為單位)
面積平方步 = π * 半徑 * 半徑

# 1 畝 = 240 平方步
a = Fraction(面積平方步, 240)  # 轉換為畝

a#----- content ends here -----

"""
"""
