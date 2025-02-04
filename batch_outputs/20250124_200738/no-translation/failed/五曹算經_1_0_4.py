"""
今有方田，廣從各五十六步。問：為田㡬何？
術曰：列田五十六步自相乘，得三千一百三十六步，以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 廣從各五十六步
廣 = 56
從 = 56

# 列田五十六步自相乘，得三千一百三十六步
積步 = 廣 * 從

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 分解畝數為整畝和餘步
a = 畝數.numerator // 畝數.denominator  # 整畝
b = 畝數.numerator % 畝數.denominator  # 餘步
#----- content ends here -----


"""

"""


"""
Variable 'b' has wrong value. Expected: 16, Actual: 1"""
