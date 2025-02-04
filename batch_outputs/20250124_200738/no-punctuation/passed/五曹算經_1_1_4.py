"""
今有方田廣從各六十八步問為田㡬何
術曰列田六十八步自相乘得四千六百二十四步以畝法除之即得
答曰 a畝 奇 b步 
"""

#----- content starts here -----
"""
Suppose there is a square field with both width and length being 68 bu.
Question: how large is the field?

The procedure says: Place the field's 68 bu, multiply it by itself, obtaining 4624 bu.
Divide it by the mu-divisor, 240, to obtain the result.

Answer: *a* mu and *b* bu.
"""

# 方田廣從各六十八步
廣 = 68
從 = 68

# 自相乘得四千六百二十四步
積步 = 廣 * 從

# 以畝法除之
畝法 = 240
畝數 = 積步 // 畝法  # Integer division to get the whole number of mu
餘步 = 積步 % 畝法   # Remainder to get the leftover bu

a = 畝數
b = 餘步#----- content ends here -----

"""
"""
