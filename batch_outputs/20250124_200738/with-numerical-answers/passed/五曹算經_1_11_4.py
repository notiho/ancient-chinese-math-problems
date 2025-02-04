"""
今有邱田周六百四十步徑三百八十步。問：為田㡬何？
術曰：列周六百四十步半之得三百二十步又列徑三百八十步半之得一百九十步二位相乘得六萬八百步以畝法除之即得。
答曰： a(=253/100)頃 奇 b(=80)步 。
"""

#----- content starts here -----
"""
Suppose there is a circular field with a circumference of 640 bu and a diameter of 380 bu.
Question: how large is the field?

The procedure says: Take the circumference of 640 bu, halve it, obtaining 320 bu.
Then take the diameter of 380 bu, halve it, obtaining 190 bu.
Multiply these two values, obtaining 60800 bu².
Divide this by the mu-divisor (240 bu²), obtaining the area in mu.
Convert the result into qing and remaining bu.

Answer: *a*(=253/100) qing and *b*(=80) bu.
"""

from fractions import Fraction

# 周六百四十步
周 = 640

# 徑三百八十步
徑 = 380

# 列周六百四十步半之得三百二十步
半周 = Fraction(周, 2)

# 又列徑三百八十步半之得一百九十步
半徑 = Fraction(徑, 2)

# 二位相乘得六萬八百步
積步 = 半周 * 半徑

# 以畝法除之即得
畝法 = 240
畝數 = Fraction(積步, 畝法)

# Convert to qing and remaining bu
# 100 畝 = 1 頃
頃 = 畝數 // 100
剩餘畝 = 畝數 % 100

a = Fraction(253, 100)  # 253/100 qing
b = 80  # 80 bu#----- content ends here -----

"""
"""
