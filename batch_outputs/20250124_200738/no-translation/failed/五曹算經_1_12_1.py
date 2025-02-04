"""
今有箕田一頭廣八十六步一頭廣四十步從九十步。問：為田㡬何？
術曰：并二廣得一百二十六步半之得六十三步以從九十步乘之得五千六百七十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 一頭廣八十六步
廣1 = 86

# 一頭廣四十步
廣2 = 40

# 從九十步
從 = 90

# 并二廣得一百二十六步
并廣 = 廣1 + 廣2

# 半之得六十三步
平均廣 = Fraction(并廣, 2)

# 以從九十步乘之得五千六百七十步
積步 = 平均廣 * 從

# 以畝法二百四十步除之即得
畝法 = 240
畝數 = Fraction(積步, 畝法)

# 分離畝數與奇步
a = 畝數.numerator // 畝數.denominator  # 整畝數
b = 畝數.numerator % 畝數.denominator   # 奇步數

# a畝 奇 b步
#----- content ends here -----


"""

"""


"""
Variable 'b' has wrong value. Expected: 150, Actual: 5"""
