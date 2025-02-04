"""
今有圓田，周三十步，徑十步。問：為田幾何？
術曰：半周半徑相乘得積步。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a circular field with a circumference of 30 bu and a diameter of 10 bu.
Question: how large is the field?

The procedure says: Multiply half the circumference by half the diameter to obtain the accumulated bu.

The answer says: *a* bu.
"""

# 周三十步
周 = 30

# 徑十步
徑 = 10

# 半周
半周 = Fraction(周, 2)

# 半徑
半徑 = Fraction(徑, 2)

# 半周半徑相乘得積步
積步 = 半周 * 半徑

a = 積步#----- content ends here -----

"""
"""
