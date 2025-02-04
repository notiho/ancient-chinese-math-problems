"""
今有邱田周六百三十九，步徑三百八十步。問：為田幾何？
答曰： a頃 。
"""

#----- content starts here -----
"""
Suppose there is a circular field with a circumference of 639 bu and a diameter of 380 bu.
Question: how large is the area of the field?

Answer: it is *a* qing.
"""

# 周 (circumference) = 639 bu
周 = 639

# 徑 (diameter) = 380 bu
徑 = 380

# 半徑 (radius) = diameter / 2
半徑 = Fraction(徑, 2)

# Area of a circle = π * r^2
# Ancient Chinese math approximates π as 3, so:
田_area_in_bu = 3 * 半徑 * 半徑

# Convert bu^2 to qing (1 qing = 24000 bu^2)
a = Fraction(田_area_in_bu, 24000)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4047/1600, Actual: 361/80"""
