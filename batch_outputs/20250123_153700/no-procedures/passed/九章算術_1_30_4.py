"""
今有圓田，周三十步，徑十步。問：為田幾何？
荅曰： a步 。
"""

"""
Suppose there is a circular field with a circumference of 30 bu and a diameter of 10 bu.
Question: how large is the area of the field?

Answer: it is *a* bu².
"""

# 圓田周三十步
周 = 30

# 圓田徑十步
徑 = 10

# 半徑 (radius) is half of the diameter
半徑 = Fraction(徑, 2)

# Area of a circle is π * r². Ancient Chinese math approximates π as 3.
π = 3

# Calculate the area
a = π * 半徑 * 半徑  # Area in square bu

a
"""
"""
