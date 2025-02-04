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
Multiply these two results together to get 60800 bu².
Divide this by the mu-divisor (240 bu² per mu) to get the area in mu.
Finally, convert the result into qing (1 qing = 100 mu) and remaining bu.

Answer: *a* qing and *b* bu.
"""

from fractions import Fraction

# 周六百四十步
周 = 640

# 徑三百八十步
徑 = 380

# 半之
周半 = 周 / 2
徑半 = 徑 / 2

# 二位相乘
積步 = 周半 * 徑半

# 畝法
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# Convert to 頃 and 奇步
a = 畝數 // 100  # 頃
b = 畝數 % 100  # 奇步

a, b#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
