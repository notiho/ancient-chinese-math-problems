"""
今有直田廣八十步從一百九十步。問：為田㡬何？
術曰：列廣八十步以從一百九十步乘之得一萬五千二百步以畝法除之即得。
答曰： a(=63)畝 奇 b(=80)步 。
"""

"""
Suppose there is a rectangular field with a width of 80 bu and a length of 190 bu.
Question: how large is the field?

The procedure says: Place the width of 80 bu and multiply it by the length of 190 bu, obtaining 15200 bu².
Divide this by the mu-divisor (240 bu² per mu), and the result is obtained.

The answer says: *a*(=63) mu and *b*(=80) bu.
"""

# 廣八十步
廣步數 = 80

# 從一百九十步
從步數 = 190

# 列廣八十步以從一百九十步乘之得一萬五千二百步
積步 = 廣步數 * 從步數  # 15200

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)  # 63 + 80/240

# 分離整畝與餘步
a = 畝數.numerator // 畝數.denominator  # 63 (整畝數)
b = 畝數.numerator % 畝數.denominator  # 80 (餘步數)
"""
Variable 'b' has wrong value. Expected: 80, Actual: 1"""
