"""
今有圓田周三百步徑一百步問得田幾何
術曰先置周三百步半之得一百五十步又置徑一百步半之得五十步相乘得七千五百步以畝法二百四十步除之即得
答曰 a畝 奇 b步 
"""

"""
Suppose there is a circular field with a circumference of 300 bu and a diameter of 100 bu.
Question: how large is the field?

The procedure says: First, take the circumference of 300 bu and halve it, obtaining 150 bu.
Then, take the diameter of 100 bu and halve it, obtaining 50 bu.
Multiply these, obtaining 7500 bu.
Divide this by the mu-divisor, 240, to obtain the result.

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# 圓田周三百步
周 = 300

# 徑一百步
徑 = 100

# 先置周三百步半之
半周 = 周 / 2

# 又置徑一百步半之
半徑 = 徑 / 2

# 相乘得七千五百步
積步 = 半周 * 半徑

# 以畝法二百四十步除之
畝法 = 240
畝數 = Fraction(積步, 畝法)

# 分解為整畝和餘步
a = 畝數.numerator // 畝數.denominator  # 整畝數
b = 畝數.numerator % 畝數.denominator  # 餘步數

a, b  # 答案: a畝 奇 b步
"""
Code error: both arguments should be Rational instances"""
