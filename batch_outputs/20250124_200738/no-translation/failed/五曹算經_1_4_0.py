"""
今有腰鼓田從八十二步两頭各廣三十步中央廣十二步。問：為田㡬何？
術曰：并三廣得七十二步以三除之得二十四步以從八十二步乘之得一千九百六十八步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 两头各广三十步
兩頭廣 = 30

# 中央廣十二步
中央廣 = 12

# 从八十二步
從步 = 82

# 并三廣得七十二步
三廣 = 兩頭廣 + 兩頭廣 + 中央廣

# 以三除之得二十四步
平均廣 = Fraction(三廣, 3)

# 以從八十二步乘之得一千九百六十八步
積步 = 平均廣 * 從步

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 分離畝與步
a = 畝數.numerator // 畝數.denominator  # 整畝數
b = 畝數.numerator % 畝數.denominator   # 剩餘步數

# 答曰：a畝 奇 b步
#----- content ends here -----


"""

"""


"""
Variable 'b' has wrong value. Expected: 48, Actual: 1"""
