"""
今有兩稅錢一千五百二十四貫二百四十文送州毎貫一十七文七分充腳於身内抽給問正錢及腳價各幾何
術曰置稅錢數以一貫文加一十七文七分為一貫一十七文七分為法除之得正錢數欲求腳價以一十七文七分為法乗正錢得腳價
答曰正錢 a貫 腳價 b貫
"""

#----- content starts here -----
"""
Suppose there are 1524 guan and 240 wen of tax money to be sent to the prefecture.
For every guan, an additional 17 wen and 7 fen are charged as a fee (jiao), which is deducted from the total.
Question: how much is the principal money (zheng qian) and how much is the fee (jiao jia)?

The procedure says: Place the total tax money.
Add 17 wen and 7 fen to 1 guan, making 1 guan 17 wen and 7 fen, which becomes the divisor.
Divide the total tax money by this divisor to obtain the principal money.
To find the fee, multiply the principal money by 17 wen and 7 fen as the divisor, obtaining the fee.

Answer: the principal money is *a* guan, and the fee is *b* guan.
"""

from fractions import Fraction

# 兩稅錢一千五百二十四貫二百四十文
稅錢 = 1524 + Fraction(240, 1000)  # Convert 240 wen to guan (1 guan = 1000 wen)

# 每貫一十七文七分
每貫腳價 = Fraction(17, 1000) + Fraction(7, 10000)  # Convert 17 wen 7 fen to guan

# 一貫加一十七文七分為一貫一十七文七分
法 = 1 + 每貫腳價

# 以稅錢除以法，得正錢數
正錢 = 稅錢 / 法

# 以一十七文七分為法，乘正錢，得腳價
腳價 = 每貫腳價 * 正錢

a = 正錢
b = 腳價#----- content ends here -----

"""
"""
