"""
今有方田廣從各六十八步。問：為田㡬何？
術曰：列田六十八步自相乘得四千六百二十四步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a square field with both its width and length being 68 bu.
Question: how large is the field?

The procedure says: Multiply the 68 bu by itself, obtaining 4624 bu².
Divide this by the mu-divisor (240 bu per mu), and the result is the area.

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# 方田廣從各六十八步
廣 = 68
從 = 68

# 自相乘得四千六百二十四步
積步 = 廣 * 從

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 分解為整畝和剩餘步數
a = 畝數.numerator // 畝數.denominator  # 整畝數
b = 畝數.numerator % 畝數.denominator  # 剩餘步數

a, b  # Output the result as (a mu, b bu)#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 64, Actual: 4"""
