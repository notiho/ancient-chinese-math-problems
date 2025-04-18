"""
今有圓田周三百步徑一百步問得田幾何
術曰先置周三百步半之得一百五十步又置徑一百步半之得五十步相乘得七千五百步以畝法二百四十步除之即得
答曰 a畝 奇 b步 
"""

#----- content starts here -----
"""
Suppose there is a circular field with a circumference of 300 bu and a diameter of 100 bu.
Question: how large is the field?

The procedure says: First, take the circumference of 300 bu and halve it, obtaining 150 bu.
Then, take the diameter of 100 bu and halve it, obtaining 50 bu.
Multiply these two results, obtaining 7500 bu.
Divide this by the mu-divisor, 240, to get the result.

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# 圓田周三百步
周 = 300

# 徑一百步
徑 = 100

# 先置周三百步半之，得一百五十步
半周 = 周 / 2

# 又置徑一百步半之，得五十步
半徑 = 徑 / 2

# 相乘，得七千五百步
積步 = 半周 * 半徑

# 以畝法二百四十步除之，即得
畝法 = 240
田 = Fraction(積步, 畝法)

# 分離整畝數與餘步數
a = int(田)  # 整畝數
b = 積步 % 畝法  # 餘步數#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
