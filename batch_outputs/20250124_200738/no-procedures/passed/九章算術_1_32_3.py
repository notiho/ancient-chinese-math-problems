"""
今有宛田，下周三十步，徑十六步。問：為田幾何？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a circular field with a circumference of 30 bu and a diameter of 16 bu.
Question: how large is the area of the field?

Answer: *a* bu².
"""

# 下周 (circumference) = 30 bu
周 = 30

# 徑 (diameter) = 16 bu
徑 = 16

# 半徑 (radius) = diameter / 2
半徑 = Fraction(徑, 2)

# Area of a circle = (circumference * radius) / 2
a = Fraction(周 * 半徑, 2)#----- content ends here -----

"""
"""
