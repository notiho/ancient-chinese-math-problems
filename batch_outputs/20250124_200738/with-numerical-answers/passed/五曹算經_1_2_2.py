"""
今有直田廣八十步從一百九十步。問：為田㡬何？
術曰：列廣八十步以從一百九十步乘之得一萬五千二百步以畝法除之即得。
答曰： a(=63)畝 奇 b(=80)步 。
"""

#----- content starts here -----
"""
Suppose there is a rectangular field with a width of 80 bu and a length of 190 bu.
Question: how large is the field?

The procedure says: Place the width of 80 bu and multiply it by the length of 190 bu, obtaining 15200 bu².
Divide this by the mu-divisor (240), and the result is the area in mu.

The answer says: *a*(=63) mu and *b*(=80) bu.
"""

# 列廣八十步
廣 = 80

# 以從一百九十步乘之
從 = 190
積步 = 廣 * 從

# 得一萬五千二百步
積步 = 15200

# 以畝法除之
畝法 = 240
畝數 = 積步 // 畝法  # 整數部分 (mu)
餘步 = 積步 % 畝法  # 餘數部分 (bu)

# 答
a = 畝數  # 63
b = 餘步  # 80#----- content ends here -----

"""
"""
