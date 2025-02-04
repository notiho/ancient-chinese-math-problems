"""
今有圭田從三十步一頭廣二十四步一頭無步。問：為田㡬何？
術曰：列一頭廣二十四步半之得一十二步以從三十步乘之得三百六十步以畝法除之即得。
答曰： a(=1)畝 奇 b(=120)步 。
"""

#----- content starts here -----
"""
Suppose there is a wedge-shaped field with one end having a width of 30 bu, the other end having a width of 24 bu, and no width at the far end.
Question: how large is the field?

The procedure says: Take the width of one end (24 bu), halve it to obtain 12 bu.
Multiply this by the length (30 bu), obtaining 360 bu.
Divide this by the mu-divisor (240 bu), obtaining the result.

The answer says: *a*(=1) mu and *b*(=120) bu.
"""

# 一頭廣二十四步
廣一頭 = 24

# 從三十步
從步 = 30

# 列一頭廣二十四步半之得一十二步
平均廣 = 廣一頭 / 2

# 以從三十步乘之得三百六十步
積步 = 平均廣 * 從步

# 以畝法除之即得
畝法 = 240
畝數 = Fraction(積步, 畝法)

# 分解畝數為整畝與餘步
a = 畝數.numerator // 畝數.denominator  # 整畝數 (1)
b = 畝數.numerator % 畝數.denominator  # 餘步數 (120)#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
