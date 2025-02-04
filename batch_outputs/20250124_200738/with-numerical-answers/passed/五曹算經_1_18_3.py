"""
今有田從一百步廣四十二步中有圓池周三十步徑一十步。問：池占外為田㡬何？
術曰：列從一百步以廣四十二步乘之得四千二百步為田積又列池周三十步半之得一十五步列徑一十步半之得五步二位相乘得七十五步為池積以減田積餘四千一百二十五步以畝法除之即得。
答曰： a(=17)畝 奇 b(=45)步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a length of 100 bu and a width of 42 bu, containing a circular pond with a circumference of 30 bu and a diameter of 10 bu.
Question: how much of the field remains after accounting for the pond?

The procedure says: Take the length of 100 bu and multiply it by the width of 42 bu, obtaining 4200 bu as the total field area.
Next, take the circumference of the pond, 30 bu, and halve it, obtaining 15 bu as the radius.
Take the diameter of the pond, 10 bu, and halve it, obtaining 5 bu as the radius (again).
Multiply these two values, obtaining 75 bu as the pond's area.
Subtract the pond's area from the total field area, leaving 4125 bu.
Divide this by the mu divisor (240 bu per mu) to obtain the result.

Answer: *a*(=17) mu and *b*(=45) bu.
"""

from fractions import Fraction

# 列從一百步
從 = 100

# 廣四十二步
廣 = 42

# 乘之得四千二百步為田積
田積 = 從 * 廣

# 列池周三十步半之得一十五步
池周 = 30
池半周 = Fraction(池周, 2)

# 列徑一十步半之得五步
池徑 = 10
池半徑 = Fraction(池徑, 2)

# 二位相乘得七十五步為池積
池積 = 池半周 * 池半徑

# 以減田積餘四千一百二十五步
餘積 = 田積 - 池積

# 以畝法除之即得
畝法 = 240
畝數 = Fraction(餘積, 畝法)

# 分離畝和步
a = 畝數.numerator // 畝數.denominator  # 17 畝
b = 餘積 % 畝法  # 45 步#----- content ends here -----

"""
"""
