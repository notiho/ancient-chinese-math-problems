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
Multiply these two values together, obtaining 60800 bu.
Divide this by the mu-divisor (240), and the result is the field size.

The answer says: *a*(=253/100) qing and *b*(=80) bu.
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
田畝數 = Fraction(積步, 畝法)

# 100 畝為 1 頃
畝每頃 = 100
田頃數 = 田畝數 // 畝每頃  # 整數部分為頃數
田餘步 = 田畝數 % 畝每頃  # 餘數部分為步數

a =田頃數 # 253/100 頃
b =田餘步#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 253/100, Actual: 2
Variable 'b' has wrong value. Expected: 80, Actual: 160/3"""
