"""
今有圭田從三十步一頭廣二十四步一頭無步。問：為田㡬何？
術曰：列一頭廣二十四步半之得一十二步以從三十步乘之得三百六十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a wedge-shaped field with one end having a width of 30 bu, the other end having a width of 24 bu, and the third side having no width (a point).
Question: how large is the field?

The procedure says: Take the width of one end, 24 bu, halve it to obtain 12 bu.
Multiply this by the length of 30 bu, obtaining 360 bu.
Divide this by the mu-divisor (240) to obtain the result.

The answer says: *a* mu and *b* bu.
"""

from fractions import Fraction

# 一頭廣二十四步
廣 = 24

# 從三十步
從 = 30

# 半之得一十二步
半廣 = 廣 / 2

# 以從三十步乘之得三百六十步
積步 = 半廣 * 從

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 分解為整畝和餘步
a = 畝數.numerator // 畝數.denominator  # 整畝數
b = 畝數.numerator % 畝數.denominator  # 餘步數#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
