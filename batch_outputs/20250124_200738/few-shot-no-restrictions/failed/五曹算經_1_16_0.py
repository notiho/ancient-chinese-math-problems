"""
今有圓田周七十八步徑二十六步。問：為田㡬何？
術曰：先列周七十八步半之得三十九步又列徑二十六步半之得一十三步二位相乘得五百七步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a circular field with a circumference of 78 bu and a diameter of 26 bu.
Question: how large is the area of the field?

The procedure says: First, take half of the circumference (78 bu), obtaining 39 bu.
Then, take half of the diameter (26 bu), obtaining 13 bu.
Multiply these two values, obtaining 507 bu².
Divide this by the mu-divisor (240 bu² per mu), and the result is the area.

The answer says: *a* mu and *b* bu².
"""

from fractions import Fraction

# 圓田周七十八步
周 = 78

# 徑二十六步
徑 = 26

# 畝法二百四十步
畝法 = 240

# 半之得三十九步
半周 = 周 / 2

# 半之得一十三步
半徑 = 徑 / 2

# 二位相乘得五百七步
積步 = 半周 * 半徑

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 分離整畝和剩餘步數
a = 畝數.numerator // 畝數.denominator  # 整畝數
b = 畝數.numerator % 畝數.denominator  # 剩餘步數

a, b#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
