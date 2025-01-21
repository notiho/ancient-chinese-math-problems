"""
今有圭田從三十步一頭廣二十四步一頭無步。問：為田㡬何？
術曰：列一頭廣二十四步半之得一十二步以從三十步乘之得三百六十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""

"""


from fractions import Fraction

# 一頭廣二十四步
廣 = 24

# 半之，得一十二步
半廣 = Fraction(廣, 2)

# 從三十步
從 = 30

# 以從三十步乘之，得三百六十步
積步 = 半廣 * 從

# 畝法二百四十步
畝法 = 240

# 以畝法除之，即得
畝數 = Fraction(積步, 畝法)

# 分離畝數與餘步
a = 畝數.numerator // 畝數.denominator  # 整畝數
b = 畝數.numerator % 畝數.denominator  # 餘步

# a畝 奇 b步


"""

"""


"""
Variable 'b' has wrong value. Expected: 120, Actual: 1"""
