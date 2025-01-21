"""
又有圓田，周一百八十一步，徑六十步三分步之一。問：為田幾何？
術曰：半周半徑相乘得積步。
荅曰： a(=32761/2880)畝 。
"""

"""
Suppose there is a circular field with a circumference of 181 bu and a diameter of 60 bu and 1/3 bu.
Question: how large is the field?

The procedure says: Multiply the half-circumference by the half-diameter to obtain the accumulated bu.

Answer: *a*(=32761/2880) mu.
"""

from fractions import Fraction

# 周一百八十一步
周 = 181

# 徑六十步三分步之一
徑 = 60 + Fraction(1, 3)

# 半周
半周 = Fraction(周, 2)

# 半徑
半徑 = Fraction(徑, 2)

# 半周半徑相乘得積步
積步 = 半周 * 半徑

# 畝法二百四十步
畝法 = 240

# 積步除以畝法得畝數
a = Fraction(積步, 畝法) # 32761/2880
"""
"""
