"""
今有方田，廣從各五十六步。問：為田㡬何？
術曰：列田五十六步自相乘，得三千一百三十六步，以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a square field, with both the width and the length being 56 bu.
Question: how large is the field?

The procedure says: Multiply the 56 bu of the field by itself, obtaining 3136 bu.
Divide it by the mu-divisor (240 bu per mu), and the result is obtained.

The answer says: *a* mu and *b* bu.
"""

from fractions import Fraction

# 廣從各五十六步
廣 = 56
從 = 56

# 列田五十六步自相乘，得三千一百三十六步
積步 = 廣 * 從

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 分解為整畝和剩餘步數
a = 畝數.numerator // 畝數.denominator  # 整畝數
b = 畝數.numerator % 畝數.denominator  # 剩餘步數

# 結果
a, b#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 16, Actual: 1"""
