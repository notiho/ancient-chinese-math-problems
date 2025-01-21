"""
今有圭田從三十步一頭廣二十四步一頭無步。問：為田㡬何？
術曰：列一頭廣二十四步半之得一十二步以從三十步乘之得三百六十步以畝法除之即得。
答曰： a(=1)畝 奇 b(=120)步 。
"""

"""
Suppose there is a wedge-shaped field with one side of length 30 bu and another side of width 24 bu, tapering to 0 bu on the opposite side.
Question: how large is the field?

The procedure says: Take the width of one side, 24 bu, halve it to obtain 12 bu.
Multiply this by the length, 30 bu, to obtain 360 bu.
Divide this by the mu-divisor (240 bu) to obtain the result.

Answer: *a*(=1) mu and *b*(=120) bu.
"""

# 一頭廣二十四步
廣 = 24

# 從三十步
從 = 30

# 列一頭廣二十四步半之得一十二步
半廣 = 廣 / 2

# 以從三十步乘之得三百六十步
積步 = 半廣 * 從

# 以畝法除之即得
畝法 = 240
畝數 = Fraction(積步, 畝法)

# 分離畝數與餘步
a = 畝數.numerator // 畝數.denominator  # 1 畝
b = 積步 % 畝法  # 120 步
"""
Code error: both arguments should be Rational instances"""
