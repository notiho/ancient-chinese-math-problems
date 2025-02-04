"""
今有圓田周三百步，徑一百步。問：得田幾何？
術曰：先置周三百步，半之，得一百五十步；又置徑一百步半之，得五十步，相乘，得七千五百步，以畝法二百四十步除之，即得。
答曰： a(=31)畝 ，奇 b(=60)步 。
"""

#----- content starts here -----
"""
Suppose there is a circular field with a circumference of 300 bu and a diameter of 100 bu.
Question: how large is the field?

The procedure says: First, place the circumference of 300 bu and halve it, obtaining 150 bu.
Then, place the diameter of 100 bu and halve it, obtaining 50 bu.
Multiply these two, obtaining 7500 bu.
Divide this by the mu-divisor, 240 bu, to obtain the result.

Answer: *a*(=31) mu, with a remainder of *b*(=60) bu.
"""

from fractions import Fraction

# 圓田周三百步
周 = 300

# 徑一百步
徑 = 100

# 先置周三百步，半之，得一百五十步
周半 = 周 / 2

# 又置徑一百步半之，得五十步
徑半 = 徑 / 2

# 相乘，得七千五百步
積步 = 周半 * 徑半

# 以畝法二百四十步除之，即得
畝法 = 240
畝數 = Fraction(積步, 畝法)

# 答曰：a(=31)畝，奇 b(=60)步
a = 畝數.numerator // 畝數.denominator  # 31 畝
b = 積步 % 畝法  # 60 步#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
