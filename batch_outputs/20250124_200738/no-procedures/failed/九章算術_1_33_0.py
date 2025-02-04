"""
又有宛田，下周九十九步，徑五十一步。問：為田幾何？
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is a circular field. The circumference is 99 bu, and the diameter is 51 bu.
Question: how large is the area of the field?

Answer: it is *a* mu.
"""

# 下周 (circumference) = 99 bu
下周 = 99

# 徑 (diameter) = 51 bu
徑 = 51

# 半徑 (radius) = diameter / 2
半徑 = Fraction(徑, 2)

# 圓面積公式: 面積 = 半徑 * 半徑 * 3 (using π ≈ 3 as per ancient Chinese math)
面積_in_bu = 半徑 * 半徑 * 3

# Convert the area from bu^2 to mu (1 mu = 240 bu^2)
a = Fraction(面積_in_bu, 240)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1683/320, Actual: 2601/320"""
