"""
今有方田廣從各六十八步問為田㡬何
術曰列田六十八步自相乘得四千六百二十四步以畝法除之即得
答曰 a畝 奇 b步 
"""

#----- content starts here -----
"""
Suppose there is a square field with both width and length being 68 bu.
Question: how large is the field?

The procedure says: Arrange the field's 68 bu, multiply it by itself, obtaining 4624 bu.
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
畝數 = Fraction(積步, 畝法)

# 分解為整畝和奇步
a = 畝數.numerator // 畝數.denominator  # 整畝數
b = 畝數.numerator % 畝數.denominator  # 奇步數#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 64, Actual: 4"""
