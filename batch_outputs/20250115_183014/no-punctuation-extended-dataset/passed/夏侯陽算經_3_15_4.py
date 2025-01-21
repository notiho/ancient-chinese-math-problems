"""
今有兩稅錢二千貫文欲送州毎貫數内抽一十文充腳問正及腳各幾何
術曰置錢數下置一貫文又加腳十文為法除之得正數卻減都錢餘即腳錢
答曰正 a貫 腳 b貫
"""

"""
Suppose there are 2000 guan of tax money, and it is desired to send it to the province.
For every guan, 10 wen are deducted as a handling fee.
Question: how much is the principal amount (zheng) and how much is the handling fee (jiao)?

The procedure says: Place the total amount of money.
Below, place one guan of money and add the handling fee of 10 wen, making the divisor.
Divide by this to obtain the principal amount.
Then subtract the principal amount from the total money, and the remainder is the handling fee.

Answer: the principal amount is *a* guan, and the handling fee is *b* guan.
"""

# 兩稅錢二千貫文
總錢 = 2000

# 一貫文
一貫文 = 1

# 加腳十文
腳 = Fraction(10, 1000)  # 10 wen is 10/1000 of a guan

# 為法
法 = 一貫文 + 腳

# 除之得正數
正數 = Fraction(總錢, 法)

# 卻減都錢餘，即腳錢
腳錢 = 總錢 - 正數

a = 正數
b = 腳錢
"""
"""
