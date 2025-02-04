"""
今有圭田從三十步一頭廣二十四步一頭無步。問：為田㡬何？
術曰：列一頭廣二十四步半之得一十二步以從三十步乘之得三百六十步以畝法除之即得。
答曰： a(=1)畝 奇 b(=120)步 。
"""

#----- content starts here -----
"""
Suppose there is a wedge-shaped field with one end having a width of 30 bu, the other end having a width of 24 bu, and no width at the far end.
Question: how large is the field?

The procedure says: Take the width of one end (24 bu), halve it to get 12 bu.
Multiply this by the length (30 bu), obtaining 360 bu.
Divide this by the mu-divisor (240), obtaining the result.

Answer: *a*(=1) mu and *b*(=120) bu.
"""

# 一頭廣二十四步
廣一頭 = 24

# 無步 (另一頭廣為零)
廣另一頭 = 0

# 從三十步
從 = 30

# 列一頭廣二十四步半之得一十二步
平均廣 = 廣一頭 / 2

# 以從三十步乘之得三百六十步
積步 = 平均廣 * 從

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
總畝數 = Fraction(積步, 畝法)

# 分離畝與奇步
a = 總畝數.numerator // 總畝數.denominator  # 1 畝
b = 積步 % 畝法  # 120 步#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
