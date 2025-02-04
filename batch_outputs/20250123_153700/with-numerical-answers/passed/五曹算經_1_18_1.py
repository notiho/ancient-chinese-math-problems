"""
今有田從一百步廣四十二步中有圓池周三十步徑一十步。問：池占外為田㡬何？
術曰：列從一百步以廣四十二步乘之得四千二百步為田積又列池周三十步半之得一十五步列徑一十步半之得五步二位相乘得七十五步為池積以減田積餘四千一百二十五步以畝法除之即得。
答曰： a(=17)畝 奇 b(=45)步 。
"""

"""
Suppose there is a field with a length of 100 bu and a width of 42 bu, within which there is a circular pond.
The pond has a circumference of 30 bu and a diameter of 10 bu.
Question: how much area does the pond occupy, and how much of the remaining area is still field?

The procedure says: Take the length of 100 bu and multiply it by the width of 42 bu, obtaining 4200 bu² as the total field area.
Then, take the pond's circumference of 30 bu, halve it to get 15 bu.
Take the diameter of 10 bu, halve it to get 5 bu.
Multiply these two values, obtaining 75 bu² as the pond's area.
Subtract the pond's area from the total field area, leaving 4125 bu².
Divide this by the mu-divisor (240 bu² per mu) to obtain the result.

Answer: *a*(=17) mu and *b*(=45) bu².
"""

from fractions import Fraction

# 田從一百步
田從 = 100

# 廣四十二步
田廣 = 42

# 列從一百步以廣四十二步乘之得四千二百步為田積
田積 = 田從 * 田廣

# 列池周三十步半之得一十五步
池周 = 30
池周半 = Fraction(池周, 2)

# 列徑一十步半之得五步
池徑 = 10
池徑半 = Fraction(池徑, 2)

# 二位相乘得七十五步為池積
池積 = 池周半 * 池徑半

# 以減田積餘四千一百二十五步
餘積 = 田積 - 池積

# 以畝法除之即得
畝法 = 240
畝數 = 餘積 // 畝法  # 整數部分
餘步 = 餘積 % 畝法  # 餘數部分

a = 畝數  # 17
b = 餘步  # 45
"""
"""
