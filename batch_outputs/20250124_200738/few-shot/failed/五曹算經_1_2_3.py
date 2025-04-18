"""
今有直田廣八十步從一百九十步。問：為田㡬何？
術曰：列廣八十步以從一百九十步乘之得一萬五千二百步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a rectangular field with a width of 80 bu and a length of 190 bu.
Question: how large is the field?

The procedure says: Place the width of 80 bu and multiply it by the length of 190 bu, obtaining 15200 bu².
Divide this by the mu-divisor (240), and the result is the area in mu.
The remainder is the number of extra bu.

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# 廣八十步
廣 = 80

# 從一百九十步
從 = 190

# 列廣八十步以從一百九十步乘之得一萬五千二百步
積步 = 廣 * 從

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 整數部分為畝數
a = 畝數.numerator // 畝數.denominator

# 餘數部分為奇步
b = 畝數.numerator % 畝數.denominator#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 80, Actual: 1"""
