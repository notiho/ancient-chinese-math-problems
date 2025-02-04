"""
今有方田廣從各五十六步問為田㡬何
術曰列田五十六步自相乘得三千一百三十六步以畝法除之即得
答曰 a畝 奇 b步 
"""

#----- content starts here -----
"""
Suppose there is a square field with both width and length being 56 bu.
Question: how large is the field?

The procedure says: Place the field's 56 bu, multiply it by itself, obtaining 3136 bu.
Divide it by the mu-divisor, 240, to obtain the result.

Answer: *a* mu and *b* bu.
"""

# 廣從各五十六步
廣 = 56
從 = 56

# 自相乘得三千一百三十六步
積步 = 廣 * 從

# 以畝法除之
畝法 = 240
畝數 = 積步 // 畝法  # 整數部分為畝數
餘步 = 積步 % 畝法  # 餘數為奇步數

a = 畝數
b = 餘步#----- content ends here -----

"""
"""
