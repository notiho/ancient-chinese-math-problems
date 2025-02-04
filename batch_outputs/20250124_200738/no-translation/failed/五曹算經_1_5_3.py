"""
今有鼓田两頭各廣四十步中央廣五十二步從八十五步。問：為田㡬何？
術曰：并三廣得一百三十二步以三除之得四十四步以從八十五步乘之得三千七百四十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 两頭各廣四十步
廣頭 = 40

# 中央廣五十二步
廣中央 = 52

# 從八十五步
從 = 85

# 并三廣得一百三十二步
三廣 = 廣頭 + 廣頭 + 廣中央

# 以三除之得四十四步
平均廣 = Fraction(三廣, 3)

# 以從八十五步乘之得三千七百四十步
積步 = 平均廣 * 從

# 以畝法二百四十步除之即得
畝法 = 240
畝數 = Fraction(積步, 畝法)

# 分解畝數為整畝和餘步
a = 畝數.numerator // 畝數.denominator  # 整畝
b = 畝數.numerator % 畝數.denominator  # 餘步

# 答案為 a 畝 奇 b 步
#----- content ends here -----


"""

"""


"""
Variable 'b' has wrong value. Expected: 140, Actual: 7"""
