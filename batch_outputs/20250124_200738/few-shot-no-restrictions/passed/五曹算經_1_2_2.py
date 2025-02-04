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
Divide this by the mu-divisor (240 bu² per mu), and the result is the area in mu and remaining bu.

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# Given dimensions
廣 = 80  # Width in bu
從 = 190  # Length in bu

# 畝法: 240 bu² per mu
畝法 = 240

# Calculate total area in bu²
積步 = 廣 * 從

# Divide by 畝法 to get the number of mu and remaining bu
畝數 = 積步 // 畝法  # Integer part (whole mu)
餘步 = 積步 % 畝法  # Remainder (remaining bu)

# Assign results
a = 畝數
b = 餘步

# Output results
a, b#----- content ends here -----

"""
"""
