"""
又有宛田下周九十九步徑五十一步問為田幾何
術曰以徑乘周四而一
荅曰 a畝 
"""

"""
Suppose there is a circular field with a circumference of 99 bu and a diameter of 51 bu.
Question: how large is the field?

The procedure says: Multiply the diameter by the circumference, then divide by 4.

The answer says: *a* mu.
"""

# 下周九十九步
周 = 99

# 徑五十一步
徑 = 51

# 以徑乘周
積步 = 徑 * 周

# 四而一
積步 = Fraction(積步, 4)

# 畝法二百四十步
畝法 = 240

# 以畝法二百四十步除之，即畝數
a = Fraction(積步, 畝法)
"""
"""
