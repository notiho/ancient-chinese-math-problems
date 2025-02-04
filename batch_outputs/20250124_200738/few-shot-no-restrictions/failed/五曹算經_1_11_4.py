"""
今有邱田周六百四十步徑三百八十步。問：為田㡬何？
術曰：列周六百四十步半之得三百二十步又列徑三百八十步半之得一百九十步二位相乘得六萬八百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a circular field with a circumference of 640 bu and a diameter of 380 bu.
Question: how large is the field?

The procedure says: Take the circumference of 640 bu, halve it to get 320 bu.
Then take the diameter of 380 bu, halve it to get 190 bu.
Multiply these two results, obtaining 60800 bu.
Divide this by the mu divisor (240 bu per mu), and you get the result.

Answer: *a* qing and *b* bu.
"""

from fractions import Fraction

# 周六百四十步
周 = 640

# 徑三百八十步
徑 = 380

# 列周六百四十步半之得三百二十步
周半 = Fraction(周, 2)

# 又列徑三百八十步半之得一百九十步
徑半 = Fraction(徑, 2)

# 二位相乘得六萬八百步
積步 = 周半 * 徑半

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 100 畝為 1 頃
畝每頃 = 100
頃 = 畝數 // 畝每頃  # 整數部分為頃數
剩餘畝 = 畝數 % 畝每頃  # 餘數為剩餘畝數

# 答案
a = int(頃)
b = float(剩餘畝)
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 253/100, Actual: 2
Variable 'b' has wrong value. Expected: 80, Actual: 53.333333333333336"""
