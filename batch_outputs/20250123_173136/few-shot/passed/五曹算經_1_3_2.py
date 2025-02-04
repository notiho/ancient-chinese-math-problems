"""
今有圭田從三十步一頭廣二十四步一頭無步。問：為田㡬何？
術曰：列一頭廣二十四步半之得一十二步以從三十步乘之得三百六十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a wedge-shaped field with one side of the length (從) being 30 bu, one side of the width (廣) being 24 bu, and the other side of the width being 0 bu.
Question: how large is the area of the field?

The procedure says: Take one side of the width (廣), halve it, obtaining 12 bu.
Multiply it by the length (從) of 30 bu, obtaining 360 bu.
Divide it by the mu-divisor (畝法), obtaining the result.

The answer says: *a* mu and *b* bu.
"""

from fractions import Fraction

# 一頭廣二十四步
廣一頭 = 24

# 一頭無步
廣另一頭 = 0

# 從三十步
從 = 30

# 畝法二百四十步
畝法 = 240

# 列一頭廣二十四步半之得一十二步
平均廣 = Fraction(廣一頭 + 廣另一頭, 2)

# 以從三十步乘之得三百六十步
積步 = 平均廣 * 從

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 分離畝數與餘步
a = 畝數.numerator // 畝數.denominator  # 整數部分為畝數
b = 積步 % 畝法  # 餘步

a, b
"""
"""
