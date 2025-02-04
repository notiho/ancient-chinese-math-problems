"""
今有圭田從三十步一頭廣二十四步一頭無步。問：為田㡬何？
術曰：列一頭廣二十四步半之得一十二步以從三十步乘之得三百六十步以畝法除之即得。
答曰： a(=1)畝 奇 b(=120)步 。
"""

#----- content starts here -----
"""
Suppose there is a wedge-shaped field with one end having a width of 30 bu, and the other end having no width (0 bu).
Question: how large is the field?

The procedure says: Take the width of one end (24 bu), halve it to obtain 12 bu.
Multiply this by the length (30 bu), obtaining 360 bu.
Divide this by the mu-divisor (240), obtaining the result.

The answer says: *a*(=1) mu and *b*(=120) bu.
"""

# 一頭廣二十四步
廣 = 24

# 從三十步
從 = 30

# 列一頭廣二十四步半之得一十二步
半廣 = 廣 / 2

# 以從三十步乘之得三百六十步
積步 = 半廣 * 從

# 以畝法除之即得
畝法 = 240
畝數 = Fraction(積步, 畝法)

# 分解為畝和步
a = 畝數.numerator // 畝數.denominator  # 整數部分為畝數 (1)
b = 積步 % 畝法  # 餘數為步數 (120)#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
