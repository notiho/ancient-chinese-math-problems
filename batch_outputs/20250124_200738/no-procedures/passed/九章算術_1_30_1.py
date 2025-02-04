"""
今有圓田，周三十步，徑十步。問：為田幾何？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a circular field with a circumference of 30 bu and a diameter of 10 bu.
Question: how large is the area of the field?

Answer: *a* bu².
"""

# 圓田周三十步
周 = 30

# 圓田徑十步
徑 = 10

# 半徑 is half of the diameter
半徑 = Fraction(徑, 2)

# 圓面積公式: π * r²
# Ancient Chinese math approximates π as 3, so:
a = 3 * 半徑 * 半徑  # Area of the circular field in bu²

a#----- content ends here -----

"""
"""
