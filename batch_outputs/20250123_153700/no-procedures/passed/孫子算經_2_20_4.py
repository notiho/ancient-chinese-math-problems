"""
今有邱田周六百三十九，步徑三百八十步。問：為田幾何？
答曰： a頃 。
"""

"""
Suppose there is a circular field with a circumference of 639 bu and a diameter of 380 bu.
Question: how large is the area of the field?

Answer: *a* qing.
"""

# 周 (circumference) = 639 bu
周 = 639

# 徑 (diameter) = 380 bu
徑 = 380

# 半徑 (radius) = diameter / 2
半徑 = Fraction(徑, 2)

# Area of a circle = (周 * 半徑) / 2
田面積 = Fraction(周 * 半徑, 2)

# Convert the area into qing (1 qing = 24000 square bu)
a = Fraction(田面積, 24000)
"""
"""
