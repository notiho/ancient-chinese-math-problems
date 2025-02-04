"""
今有圓材徑二尺五寸，欲為方版，令厚七寸。問︰廣幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a cylindrical log with a diameter of 2 chi and 5 cun (2.5 chi). It is desired to cut it into a square plank with a thickness of 7 cun (0.7 chi).  
Question: what is the width of the square plank?

Answer: the width is *a* chi.
"""

# 圓材徑二尺五寸
直徑 = Fraction(25, 10)  # 2 chi 5 cun = 2.5 chi
半徑 = 直徑 / 2

# 厚七寸
厚度 = Fraction(7, 10)  # 7 cun = 0.7 chi

# The width of the square plank is determined by the largest square that can fit within the circular cross-section.
# Using the Pythagorean theorem, the diagonal of the square equals the diameter of the circle.
# The diagonal of the square is related to its width (廣) as: diagonal = width * sqrt(2).
# Therefore, width = diameter / sqrt(2).

a = 半徑 * Fraction(2, 1)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 12/5, Actual: 5/2"""
