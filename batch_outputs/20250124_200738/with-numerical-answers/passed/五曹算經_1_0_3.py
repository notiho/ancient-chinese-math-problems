"""
今有方田，廣從各五十六步。問：為田㡬何？
術曰：列田五十六步自相乘，得三千一百三十六步，以畝法除之即得。
答曰： a(=13)畝 奇 b(=16)步 。
"""

#----- content starts here -----
"""
Suppose there is a square field with both width and length being 56 bu.
Question: how large is the field?

The procedure says: Multiply the 56 bu of the field by itself, obtaining 3136 bu.
Divide it by the mu-divisor to obtain the result.

Answer: *a*(=13) mu and remainder *b*(=16) bu.
"""

# 廣從各五十六步
廣 = 56
從 = 56

# 列田五十六步自相乘，得三千一百三十六步
積步 = 廣 * 從

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
a = 積步 // 畝法  # 13 畝
b = 積步 % 畝法  # 16 步#----- content ends here -----

"""
"""
