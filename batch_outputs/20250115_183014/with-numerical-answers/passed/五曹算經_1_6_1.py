"""
今有弧田弦八十步矢五步。問：為田㡬何？
術曰：列弦八十步半之得四十步以矢五步乘之即得。
答曰： a(=200)步 。
"""

"""
Suppose there is an arc-shaped field with a chord length of 80 bu and an arrow height of 5 bu.
Question: how large is the field?

The procedure says: Take the chord length of 80 bu, halve it to get 40 bu.
Multiply it by the arrow height of 5 bu, and the result is obtained.

Answer: *a*(=200) bu.
"""

# 弦八十步
弦 = 80

# 矢五步
矢 = 5

# 半之得四十步
半弦 = 弦 / 2

# 以矢五步乘之即得
a = 半弦 * 矢 # 200
"""
"""
