"""
今有圓材徑二尺五寸，欲為方版，令厚七寸。問︰廣幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a cylindrical log with a diameter of 2 chi and 5 cun (2.5 chi). It is desired to cut it into a rectangular plank with a thickness of 7 cun (0.7 chi).
Question: how wide can the plank be?

Answer: the width of the plank is *a* chi.
"""

# 圓材徑二尺五寸
直徑 = 2 + Fraction(5, 10)

# 厚七寸
厚 = Fraction(7, 10)

# The width of the plank is determined by the largest square that can fit within the circle.
# Using the Pythagorean theorem: width^2 + thickness^2 = diameter^2
# Solve for width:
a = (直徑**2 - 厚**2).sqrt()  # Width of the plank in chi#----- content ends here -----

"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
