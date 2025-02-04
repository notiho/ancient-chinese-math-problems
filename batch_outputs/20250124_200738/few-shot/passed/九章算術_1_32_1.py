"""
今有宛田，下周三十步，徑十六步。問：為田幾何？
術曰：以徑乘周，四而一。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a circular field. The circumference is 30 bu, and the diameter is 16 bu.
Question: how large is the area of the field?

The procedure says: Multiply the diameter by the circumference, and divide by 4.

The answer says: *a* bu.
"""

# 下周三十步
周 = 30

# 徑十六步
徑 = 16

# 以徑乘周
積 = 徑 * 周

# 四而一
a = Fraction(積, 4)#----- content ends here -----

"""
"""
