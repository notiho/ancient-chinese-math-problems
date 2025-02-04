"""
今有圓田周三百步，徑一百步。問：得田幾何？
術曰：先置周三百步，半之，得一百五十步；又置徑一百步半之，得五十步，相乘，得七千五百步，以畝法二百四十步除之，即得。
答曰： a畝 ，奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a circular field with a circumference of 300 bu and a diameter of 100 bu.
Question: how much area does the field have?

The procedure says: First, take the circumference of 300 bu and halve it, obtaining 150 bu.
Then, take the diameter of 100 bu and halve it, obtaining 50 bu.
Multiply these two results, obtaining 7500 bu².
Divide this by the mu-divisor, 240, to obtain the area in mu.

The answer says: *a* mu, with a remainder of *b* bu².
"""

from fractions import Fraction

# 圓田周三百步
周 = 300

# 徑一百步
徑 = 100

# 畝法二百四十步
畝法 = 240

# 周半之
周半 = 周 / 2

# 徑半之
徑半 = 徑 / 2

# 相乘，得積步
積步 = 周半 * 徑半

# 以畝法二百四十步除之
畝數 = Fraction(積步, 畝法)

# 分離整數部分和餘數
a = 畝數.numerator // 畝數.denominator  # 整數部分
b = 畝數.numerator % 畝數.denominator  # 餘數

# 結果
a_mu = a
b_bu = b

# a_mu represents the number of mu, and b_bu represents the remainder in bu².
#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
