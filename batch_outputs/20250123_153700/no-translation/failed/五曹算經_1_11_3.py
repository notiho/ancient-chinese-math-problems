"""
今有邱田周六百四十步徑三百八十步。問：為田㡬何？
術曰：列周六百四十步半之得三百二十步又列徑三百八十步半之得一百九十步二位相乘得六萬八百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

"""

"""


from fractions import Fraction

# 周六百四十步
周 = 640

# 徑三百八十步
徑 = 380

# 列周六百四十步半之得三百二十步
周半 = Fraction(周, 2)

# 又列徑三百八十步半之得一百九十步
徑半 = Fraction(徑, 2)

# 二位相乘得六萬八百步
積步 = 周半 * 徑半

# 以畝法除之即得
畝法 = 240
畝數 = Fraction(積步, 畝法)

# 百畝為一頃
頃 = 畝數 // 100
剩餘步 = 畝數 % 100

a = int(頃)  # 頃
b = 剩餘步  # 奇 b步


"""

"""


"""
Variable 'a' has wrong value. Expected: 253/100, Actual: 2
Variable 'b' has wrong value. Expected: 80, Actual: 160/3"""
