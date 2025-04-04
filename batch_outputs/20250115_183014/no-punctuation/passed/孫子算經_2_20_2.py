"""
今有邱田周六百三十九步徑三百八十步問為田幾何
術曰半周得三百一十九步五分半徑得一百九十步二位相乘得六萬七百五步以畝法除之即得
答曰 a頃 
"""

"""
Suppose there is a mound-shaped field with a circumference of 639 bu and a diameter of 380 bu.
Question: how large is the field?

The procedure says: Halve the circumference, obtaining 319 bu.
Take half of the diameter, obtaining 190 bu.
Multiply these two values, obtaining 60705 bu.
Divide by the mu-divisor, 240, to obtain the result.

The answer says: *a* qing.
"""

# 周六百三十九步
周 = 639

# 徑三百八十步
徑 = 380

# 半周得三百一十九步
半周 = Fraction(周, 2)

# 五分半徑得一百九十步
半徑 = Fraction(徑, 2)

# 二位相乘得六萬七百五步
積步 = 半周 * 半徑

# 以畝法除之
畝法 = 240
畝數 = Fraction(積步, 畝法)

# 100 畝為 1 頃
a = Fraction(畝數, 100)
"""
"""
