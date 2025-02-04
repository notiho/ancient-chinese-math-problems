"""
今有方田廣從各六十八步。問：為田㡬何？
術曰：列田六十八步自相乘得四千六百二十四步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""

"""


from fractions import Fraction

# 廣從各六十八步
廣從 = 68

# 列田六十八步自相乘得四千六百二十四步
積步 = 廣從 * 廣從

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 分解為畝和步
a = 畝數.numerator // 畝數.denominator  # 整畝數
b = 畝數.numerator % 畝數.denominator  # 剩餘步數

# 答案為 a畝 奇 b步


"""

"""


"""
Variable 'b' has wrong value. Expected: 64, Actual: 4"""
