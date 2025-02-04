"""
今有宛田，下周三十步，徑十六步。問：為田幾何？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a circular field. Its circumference is 30 bu, and its diameter is 16 bu.
Question: how large is the area of the field?

Answer: the area is *a* bu².
"""

# 下周三十步 (circumference)
周 = 30

# 徑十六步 (diameter)
徑 = 16

# 半徑 (radius) = diameter / 2
半徑 = Fraction(徑, 2)

# Area of a circle = (radius² * π), where π is approximated as 3
a = 半徑 * 半徑 * 3  # Using π ≈ 3 as per ancient Chinese approximation

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 120, Actual: 192"""
