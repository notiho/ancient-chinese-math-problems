"""
今有邱田周六百三十九，步徑三百八十步。問：為田幾何？
術曰：半周得三百一十九步五分半徑，得一百九十步二位相乘，得六萬七百五步，以畝法除之，即得。
答曰： a頃 。
"""

#----- content starts here -----
"""
Suppose there is a circular field with a circumference of 639 bu and a diameter of 380 bu.
Question: how large is the field?

The procedure says: Halve the circumference, obtaining 319.5 bu.
Halve the diameter, obtaining 190 bu.
Multiply these two values together, obtaining 60705 bu².
Divide this by the mu-divisor (240), and the result is the area in mu.

The answer says: *a* qing.
"""

from fractions import Fraction

# 周六百三十九
周 = 639

# 步徑三百八十步
徑 = 380

# 半周得三百一十九步五
半周 = Fraction(周, 2)

# 半徑，得一百九十步
半徑 = Fraction(徑, 2)

# 二位相乘，得六萬七百五步
積步 = 半周 * 半徑

# 畝法二百四十步
畝法 = 240

# 以畝法除之，即得畝數
畝數 = Fraction(積步, 畝法)

# 100 畝為 1 頃
頃數 = Fraction(畝數, 100)

a = 頃數
#----- content ends here -----

"""
"""
