"""
今有圭田從三十步一頭廣二十四步一頭無步問為田㡬何
術曰列一頭廣二十四步半之得一十二步以從三十步乘之得三百六十步以畝法除之即得
答曰 a畝 奇 b步 
"""

"""
Suppose there is a wedge-shaped field. One end has a length of 30 bu, and the other end has a width of 24 bu, while the narrow end has no width.
Question: how large is the field?

The procedure says: Take the width of one end, 24 bu, and halve it, obtaining 12 bu.
Multiply this by the length, 30 bu, obtaining 360 bu.
Divide this by the mu-divisor, 240, to obtain the result.

Answer: *a* mu and *b* bu.
"""

# 一頭廣二十四步
廣 = 24

# 半之，得一十二步
半廣 = 廣 / 2

# 從三十步
從 = 30

# 以從三十步乘之，得三百六十步
積步 = 半廣 * 從

# 畝法二百四十步
畝法 = 240

# 以畝法除之，即得
畝數 = Fraction(積步, 畝法)

# 分解為整畝和餘步
a = 畝數.numerator // 畝數.denominator  # 整畝
b = 畝數.numerator % 畝數.denominator  # 餘步
"""
Code error: both arguments should be Rational instances"""
