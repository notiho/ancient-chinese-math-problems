"""
今有圓田周七十八步徑二十六步。問：為田㡬何？
術曰：先列周七十八步半之得三十九步又列徑二十六步半之得一十三步二位相乘得五百七步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""

"""


from fractions import Fraction

# 圓田周七十八步
周 = 78

# 徑二十六步
徑 = 26

# 先列周七十八步半之得三十九步
半周 = Fraction(周, 2)

# 又列徑二十六步半之得一十三步
半徑 = Fraction(徑, 2)

# 二位相乘得五百七步
積步 = 半周 * 半徑

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 分離畝數與餘步
a = 畝數.numerator // 畝數.denominator  # 整數部分為畝
b = 畝數.numerator % 畝數.denominator   # 餘數部分為步

# 答曰：a畝 奇 b步


"""

"""


"""
Variable 'b' has wrong value. Expected: 27, Actual: 9"""
