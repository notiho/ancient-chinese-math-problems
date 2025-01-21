"""
今有兩稅錢一千五百二十四貫二百四十文送州毎貫一十七文七分充腳於身内抽給問正錢及腳價各幾何
術曰置稅錢數以一貫文加一十七文七分為一貫一十七文七分為法除之得正錢數欲求腳價以一十七文七分為法乗正錢得腳價
答曰正錢 a貫 腳價 b貫
"""

"""
Suppose there are 1524 guan and 240 wen of tax money to be sent to the prefecture. 
For every guan, an additional 17 wen and 7 fen are charged as a fee (jiao), which is deducted from the total tax money.
Question: how much is the principal tax money (zheng qian) and how much is the fee (jiao jia)?

The procedure says: Place the total tax money. 
Add 17 wen and 7 fen to 1 guan, making 1 guan 17 wen and 7 fen, which becomes the divisor.
Divide the total tax money by this divisor to obtain the principal tax money.
To find the fee, use 17 wen and 7 fen as the multiplier and multiply it by the principal tax money to obtain the fee.

Answer: the principal tax money is *a* guan, and the fee is *b* guan.
"""

from fractions import Fraction

# 兩稅錢一千五百二十四貫二百四十文
稅錢 = 1524 + Fraction(240, 1000)  # Convert 240 wen to guan (1 guan = 1000 wen)

# 每貫一十七文七分
每貫腳價 = 17 + Fraction(7, 10) / 1000  # Convert 17 wen and 7 fen to guan

# 一貫一十七文七分為法
法 = 1 + 每貫腳價

# 以稅錢數除以法，得正錢數
正錢 = 稅錢 / 法

# 以一十七文七分為法，乘正錢，得腳價
腳價 = 每貫腳價 * 正錢

a = 正錢
b = 腳價
"""
Variable 'a' has wrong value. Expected: 15242400/10177, Actual: 15242400/180007
Variable 'b' has wrong value. Expected: 6744762/254425, Actual: 6478286742/4500175"""
