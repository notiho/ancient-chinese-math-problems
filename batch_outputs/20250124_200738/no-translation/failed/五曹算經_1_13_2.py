"""
今有四不等田東三十五步西四十五步南二十五步北一十五步。問：為田㡬何？
術曰：并東西得八十步半之得四十步又并南北得四十步半之得二十步二位相乘得八百步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 東三十五步
東 = 35

# 西四十五步
西 = 45

# 南二十五步
南 = 25

# 北一十五步
北 = 15

# 并東西得八十步，半之得四十步
東西平均 = (東 + 西) / 2

# 并南北得四十步，半之得二十步
南北平均 = (南 + 北) / 2

# 二位相乘得八百步
積步 = 東西平均 * 南北平均

# 以畝法除之即得
畝法 = 240
畝數 = Fraction(積步, 畝法)

# 分離畝數與餘步
a = 畝數.numerator // 畝數.denominator  # 整數部分為畝數
b = 畝數.numerator % 畝數.denominator  # 餘數部分為步數

# 答曰：a畝 奇 b步
#----- content ends here -----


"""

"""


"""
Code error: both arguments should be Rational instances"""
