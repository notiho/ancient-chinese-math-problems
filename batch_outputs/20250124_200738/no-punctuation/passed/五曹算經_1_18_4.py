"""
今有田從一百步廣四十二步中有圓池周三十步徑一十步問池占外為田㡬何
術曰列從一百步以廣四十二步乘之得四千二百步為田積又列池周三十步半之得一十五步列徑一十步半之得五步二位相乘得七十五步為池積以減田積餘四千一百二十五步以畝法除之即得
答曰 a畝 奇 b步 
"""

#----- content starts here -----
"""
Suppose there is a rectangular field with a length of 100 bu and a width of 42 bu. 
Within it, there is a circular pond with a circumference of 30 bu and a diameter of 10 bu.
Question: how much of the field remains after accounting for the pond?

The procedure says: Place the length of 100 bu and multiply it by the width of 42 bu, obtaining 4200 bu as the total field area.
Then, place the circumference of the pond, 30 bu, and halve it, obtaining 15 bu as the radius.
Place the diameter, 10 bu, and halve it, obtaining 5 bu as the radius.
Multiply the two radii, obtaining 75 bu as the pond area.
Subtract the pond area from the total field area, leaving 4125 bu.
Divide by the mu-divisor (240 bu), and the result is the remaining area.

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# 列從一百步
從 = 100

# 廣四十二步
廣 = 42

# 以廣四十二步乘之，得四千二百步，為田積
田積 = 從 * 廣

# 列池周三十步，半之，得一十五步
池周 = 30
池半周 = Fraction(池周, 2)

# 列徑一十步，半之，得五步
池徑 = 10
池半徑 = Fraction(池徑, 2)

# 二位相乘，得七十五步，為池積
池積 = 池半周 * 池半徑

# 以減田積，餘四千一百二十五步
餘積 = 田積 - 池積

# 以畝法除之，即得
畝法 = 240
a = 餘積 // 畝法  # 整數部分為畝數
b = 餘積 % 畝法  # 餘數部分為步數#----- content ends here -----

"""
"""
