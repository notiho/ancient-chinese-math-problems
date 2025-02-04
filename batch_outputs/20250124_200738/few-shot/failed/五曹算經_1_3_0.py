"""
今有圭田從三十步一頭廣二十四步一頭無步。問：為田㡬何？
術曰：列一頭廣二十四步半之得一十二步以從三十步乘之得三百六十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a wedge-shaped field, with one end having a width of 30 bu, the other end having a width of 24 bu, and no width at the far end.
Question: how large is the field?

The procedure says: Take the width of one end, 24 bu, halve it to obtain 12 bu.
Multiply this by the length, 30 bu, to obtain 360 bu.
Divide this by the mu-divisor to obtain the result.

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# 一頭廣二十四步
廣一頭 = 24

# 半之得一十二步
廣半 = 廣一頭 / 2

# 從三十步
從步 = 30

# 以從三十步乘之
積步 = 廣半 * 從步

# 畝法二百四十步
畝法 = 240

# 以畝法除之
畝數 = Fraction(積步, 畝法)

# 分解為畝和步
a = 畝數.numerator // 畝數.denominator  # 整畝數
b = 畝數.numerator % 畝數.denominator  # 剩餘步數

a, b#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
