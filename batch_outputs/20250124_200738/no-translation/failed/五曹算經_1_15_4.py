"""
今有田形如牛角從五十步口廣二十步。問：為田㡬何？
術曰：列口廣二十步半之得十步以從五十步乘之得五百步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 口廣二十步
口廣 = 20

# 半之，得十步
半口廣 = 口廣 / 2

# 從五十步
從 = 50

# 以半口廣乘從，得五百步
積步 = 半口廣 * 從

# 畝法二百四十步
畝法 = 240

# 以畝法除之，即得畝數
畝數 = Fraction(積步, 畝法)

# 分離畝數與餘步
a = 畝數.numerator // 畝數.denominator  # 整畝數
b = 積步 % 畝法  # 餘步
#----- content ends here -----


"""

"""


"""
Code error: both arguments should be Rational instances"""
