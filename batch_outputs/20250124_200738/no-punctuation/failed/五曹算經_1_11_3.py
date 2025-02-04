"""
今有邱田周六百四十步徑三百八十步問為田㡬何
術曰列周六百四十步半之得三百二十步又列徑三百八十步半之得一百九十步二位相乘得六萬八百步以畝法除之即得
答曰 a頃 奇 b步 
"""

#----- content starts here -----
"""
Suppose there is a circular field with a circumference of 640 bu and a diameter of 380 bu.
Question: how large is the field?

The procedure says: Take the circumference of 640 bu, halve it, obtaining 320 bu.
Then take the diameter of 380 bu, halve it, obtaining 190 bu.
Multiply these two values, obtaining 60800 bu.
Divide this by the mu-divisor (240), obtaining the result.

Answer: *a* qing and *b* bu.
"""

from fractions import Fraction

# 周六百四十步
周 = 640

# 徑三百八十步
徑 = 380

# 半之得三百二十步 (for 周)
半周 = 周 / 2

# 半之得一百九十步 (for 徑)
半徑 = 徑 / 2

# 二位相乘得六萬八百步
積步 = 半周 * 半徑

# 以畝法除之
畝法 = 240
畝數 = Fraction(積步, 畝法)

# Convert to qing and remaining bu
a = 畝數 // 100  # 1 qing = 100 mu
b = 畝數 % 100  # Remaining mu#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
