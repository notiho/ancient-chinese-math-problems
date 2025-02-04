"""
今有方田廣從各五十六步問為田㡬何
術曰列田五十六步自相乘得三千一百三十六步以畝法除之即得
答曰 a畝 奇 b步 
"""

"""
Suppose there is a square field with both the width and length being 56 bu.
Question: how large is the field?

The procedure says: Place the field's 56 bu, multiply it by itself, obtaining 3136 bu.
Divide it by the mu-divisor, and the result is the number of mu.
The remainder is the number of bu.

Answer: *a* mu and *b* bu.
"""

# 廣從各五十六步
廣 = 56
從 = 56

# 自相乘得三千一百三十六步
積步 = 廣 * 從

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
a = 積步 // 畝法  # 整數部分為畝數
b = 積步 % 畝法  # 餘數部分為步數
"""
"""
