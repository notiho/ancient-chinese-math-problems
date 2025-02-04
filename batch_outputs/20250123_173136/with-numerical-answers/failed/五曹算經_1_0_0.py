"""
今有方田，廣從各五十六步。問：為田㡬何？
術曰：列田五十六步自相乘，得三千一百三十六步，以畝法除之即得。
答曰： a(=13)畝 奇 b(=16)步 。
"""

"""
Suppose there is a square field, with both the width and the length being 56 bu.
Question: how large is the field?

The procedure says: Place the 56 bu of the field and multiply it by itself, obtaining 3136 bu.
Divide it by the mu-divisor to obtain the result.

Answer: *a*(=13) mu and remainder *b*(=16) bu.
"""

from fractions import Fraction

# 廣從各五十六步
廣 = 56
從 = 56

# 列田五十六步自相乘
積步 = 廣 * 從

# 畝法
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 整數部分為畝
a = 畝數.numerator // 畝數.denominator  # 13

# 餘數部分為奇步
b = 畝數.numerator % 畝數.denominator  # 16
"""
Variable 'b' has wrong value. Expected: 16, Actual: 1"""
