"""
今有邱田周六百三十九，步徑三百八十步。問：為田幾何？
術曰：半周得三百一十九步五分半徑，得一百九十步二位相乘，得六萬七百五步，以畝法除之，即得。
答曰： a(=4047/1600)頃 。
"""

"""
Suppose there is a circular field with a circumference of 639 bu and a diameter of 380 bu.
Question: how large is the field?

The procedure says: Take half of the circumference, obtaining 319.5 bu.
Take half of the diameter, obtaining 190 bu.
Multiply these two values together, obtaining 60705 bu².
Divide this by the mu-divisor (240), and then convert to qing (100 mu = 1 qing).

Answer: *a*(=4047/1600) qing.
"""

from fractions import Fraction

# 邱田周六百三十九
周 = 639

# 步徑三百八十步
徑 = 380

# 半周得三百一十九步五分
半周 = Fraction(周, 2)  # 319.5

# 半徑，得一百九十步
半徑 = Fraction(徑, 2)  # 190

# 二位相乘，得六萬七百五步
積步 = 半周 * 半徑  # 60705

# 畝法二百四十步
畝法 = 240

# 以畝法除之，即得畝數
畝數 = Fraction(積步, 畝法)

# 100 畝為 1 頃
a = Fraction(畝數, 100)  # 4047/1600 qing
"""
"""
