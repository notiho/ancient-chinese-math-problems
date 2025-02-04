"""
又有圓田，周一百八十一步，徑六十步三分步之一。問：為田幾何？
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is a circular field with a circumference of 181 bu and a diameter of 60 + 1/3 bu.
Question: how large is the area of the field?

Answer: the area is *a* mu.
"""

from fractions import Fraction

# 周 (circumference) = 181 bu
周 = 181

# 徑 (diameter) = 60 + 1/3 bu
徑 = 60 + Fraction(1, 3)

# 半徑 (radius) = diameter / 2
半徑 = 徑 / 2

# 圓面積公式: 面積 = π * 半徑^2
# Ancient Chinese approximation for π is 3
π = 3

# 面積 in square bu
面積 = π * 半徑**2

# Convert square bu to mu (1 mu = 240 square bu)
a = Fraction(面積, 240)

a#----- content ends here -----

"""
"""
