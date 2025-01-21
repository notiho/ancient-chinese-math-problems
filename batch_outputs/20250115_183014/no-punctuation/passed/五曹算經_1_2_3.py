"""
今有直田廣八十步從一百九十步問為田㡬何
術曰列廣八十步以從一百九十步乘之得一萬五千二百步以畝法除之即得
答曰 a畝 奇 b步 
"""

"""
Suppose there is a rectangular field with a width of 80 bu and a length of 190 bu.
Question: how large is the field?

The procedure says: Place the width of 80 bu, and multiply it by the length of 190 bu, obtaining 15200 bu.
Divide it by the mu divisor (240), obtaining the number of mu.
The remainder is the number of extra bu.

Answer: *a* mu and *b* bu.
"""

# 廣八十步
廣步數 = 80

# 從一百九十步
從步數 = 190

# 以從一百九十步乘之，得一萬五千二百步
積步 = 廣步數 * 從步數

# 畝法二百四十步
畝法 = 240

# 以畝法除之，即得
a = 積步 // 畝法  # 整數部分為畝數
b = 積步 % 畝法  # 餘數部分為奇步數
"""
"""
