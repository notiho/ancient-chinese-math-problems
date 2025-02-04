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

# 圓田周七十八步
周 = 78

# 圓田徑二十六步
徑 = 26

# 半徑 = 徑 / 2
半徑 = Fraction(徑, 2)

# 圓面積公式: 面積 = π * 半徑²
# Ancient Chinese approximated π as 3, so:
π = 3
面積 = π * 半徑 * 半徑

# Convert the area into mu and bu²
# 1 畝 = 240 bu²
a = 面積 // 240  # Integer part in mu
b = 面積 % 240   # Remainder in bu²

a, b  # Output the result as (a 畝, b bu²)#----- content ends here -----

"""
"""
