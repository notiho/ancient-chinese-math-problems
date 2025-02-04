"""
今有方田廣從各六十八步。問：為田㡬何？
術曰：列田六十八步自相乘得四千六百二十四步以畝法除之即得。
答曰： a(=19)畝 奇 b(=64)步 。
"""

#----- content starts here -----
"""
Suppose there is a square field with both the width and length being 68 bu.
Question: how large is the field?

The procedure says: Place the 68 bu of the field and multiply it by itself, obtaining 4624 bu.
Divide it by the mu-divisor, and the result is obtained.

Answer: *a*(=19) mu and remainder *b*(=64) bu.
"""

from fractions import Fraction

# 方田廣從各六十八步
廣 = 68
從 = 68

# 列田六十八步自相乘得四千六百二十四步
積步 = 廣 * 從

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 整數部分為畝
a = 畝數.numerator // 畝數.denominator  # 19

# 餘數部分為步
b = 畝數.numerator % 畝數.denominator  # 64#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 64, Actual: 4"""
