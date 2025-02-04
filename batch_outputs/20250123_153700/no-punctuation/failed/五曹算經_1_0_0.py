"""
今有方田廣從各五十六步問為田㡬何
術曰列田五十六步自相乘得三千一百三十六步以畝法除之即得
答曰 a畝 奇 b步 
"""

"""
Suppose there is a square field with both the width and the length being 56 bu.
Question: how large is the field?

The procedure says: Place the field's 56 bu, multiply it by itself, obtaining 3136 bu.
Divide it by the mu-divisor, 240, to obtain the result.

The answer says: *a* mu and *b* bu.
"""

# 方田廣從各五十六步
廣 = 56
從 = 56

# 自相乘得三千一百三十六步
積步 = 廣 * 從

# 以畝法除之
畝法 = 240
畝數 = Fraction(積步, 畝法)

# 分離畝和步
a = 畝數.numerator // 畝數.denominator  # 整畝數
b = 畝數.numerator % 畝數.denominator  # 剩餘步數
"""
Variable 'b' has wrong value. Expected: 16, Actual: 1"""
