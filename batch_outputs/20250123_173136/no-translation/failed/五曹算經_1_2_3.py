"""
今有直田廣八十步從一百九十步。問：為田㡬何？
術曰：列廣八十步以從一百九十步乘之得一萬五千二百步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""

"""


from fractions import Fraction

# 列廣八十步
廣 = 80

# 從一百九十步
從 = 190

# 以從一百九十步乘之得一萬五千二百步
積步 = 廣 * 從

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 分解為畝和步
a = 畝數.numerator // 畝數.denominator  # 整數部分為畝
b = 畝數.numerator % 畝數.denominator   # 餘數部分為步


"""

"""


"""
Variable 'b' has wrong value. Expected: 80, Actual: 1"""
