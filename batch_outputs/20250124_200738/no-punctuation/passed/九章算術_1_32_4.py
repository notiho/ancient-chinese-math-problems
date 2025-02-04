"""
今有宛田下周三十步徑十六步問為田幾何
術曰以徑乘周四而一
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose there is a circular field with a circumference of 30 bu and a diameter of 16 bu.
Question: how large is the area of the field?

The procedure says: Multiply the diameter by the circumference, then divide by 4.

The answer says: *a* bu².
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
