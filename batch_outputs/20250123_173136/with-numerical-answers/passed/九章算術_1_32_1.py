"""
今有宛田，下周三十步，徑十六步。問：為田幾何？
術曰：以徑乘周，四而一。
荅曰： a(=120)步 。
"""

"""
Suppose there is a circular field with a circumference of 30 bu and a diameter of 16 bu.
Question: how large is the area of the field?

The procedure says: Multiply the diameter by the circumference, and divide by 4.

The answer says: *a*(=120) bu².
"""

# 下周三十步
周 = 30

# 徑十六步
徑 = 16

# 以徑乘周
積 = 徑 * 周

# 四而一
a = Fraction(積, 4) # 120
"""
"""
