"""
今有直田廣八十步從一百九十步。問：為田㡬何？
術曰：列廣八十步以從一百九十步乘之得一萬五千二百步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a rectangular field with a width of 80 bu and a length of 190 bu.
Question: how large is the field?

The procedure says: Place the width of 80 bu and multiply it by the length of 190 bu, obtaining 15200 bu.
Divide this by the mu-divisor (240), and the result is the field size in mu.
The remainder is the leftover bu.

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# 廣八十步
廣 = 80

# 從一百九十步
從 = 190

# 列廣八十步以從一百九十步乘之得一萬五千二百步
積步 = 廣 * 從

# 畝法
畝法 = 240

# 以畝法除之即得
畝數 = 積步 // 畝法  # Integer division gives the number of full mu
餘步 = 積步 % 畝法   # Remainder gives the leftover bu

a = 畝數
b = 餘步#----- content ends here -----

"""
"""
