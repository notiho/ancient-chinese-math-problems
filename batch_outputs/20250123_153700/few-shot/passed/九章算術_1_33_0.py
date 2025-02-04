"""
又有宛田，下周九十九步，徑五十一步。問：為田幾何？
術曰：以徑乘周，四而一。
荅曰： a畝 。
"""

"""
Suppose there is a circular field. Its circumference is 99 bu, and its diameter is 51 bu.
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
田步 = Fraction(積步, 4)

# 畝法二百四十步
畝法 = 240

# 以畝法除之，即畝數
a = Fraction(田步, 畝法)
"""
"""
