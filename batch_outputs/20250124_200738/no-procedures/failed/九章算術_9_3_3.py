"""
今有圓材徑二尺五寸，欲為方版，令厚七寸。問︰廣幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a cylindrical log with a diameter of 2 chi and 5 cun. It is desired to cut it into a square plank with a thickness of 7 cun.
Question: what is the width of the square plank?

Answer: the width is *a* chi.
"""

# 圓材徑二尺五寸 (convert to chi)
直徑 = 2 + Fraction(5, 10)

# 半徑
半徑 = 直徑 / 2

# 厚七寸 (convert to chi)
厚 = Fraction(7, 10)

# The width of the square plank is determined by the largest square that can fit within the circular cross-section.
# Using the Pythagorean theorem: width^2 + thickness^2 = diameter^2
a = (半徑**2 - (厚 / 2)**2)**0.5#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 12/5, Actual: 1.2"""
