"""
今有圓田周七十八步徑二十六步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a circular field with a circumference of 78 bu and a diameter of 26 bu.
Question: how large is the area of the field?

Answer: *a* mu and *b* bu.
"""

# 圓田周七十八步 (Circumference = 78 bu)
周 = 78

# 徑二十六步 (Diameter = 26 bu)
徑 = 26

# 半徑 (Radius) = Diameter / 2
半徑 = Fraction(徑, 2)

# 圓面積公式 (Area of a circle) = π * r^2
# Ancient Chinese math approximates π as 3
圓面積 = 3 * 半徑 * 半徑

# Convert the area into mu and bu
# 1 畝 = 240 bu
a = 圓面積 // 240  # Integer part in mu
b = 圓面積 % 240   # Remainder in bu

a, b  # Final result: a mu and b bu#----- content ends here -----

"""
"""
