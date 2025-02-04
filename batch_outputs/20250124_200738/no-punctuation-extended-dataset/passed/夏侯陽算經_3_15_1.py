"""
今有兩稅錢二千貫文欲送州毎貫數内抽一十文充腳問正及腳各幾何
術曰置錢數下置一貫文又加腳十文為法除之得正數卻減都錢餘即腳錢
答曰正 a貫 腳 b貫
"""

#----- content starts here -----
"""
Suppose there are 2000 guan of tax money. It is desired to send it to the prefecture, and for every guan, 10 wen are deducted as a handling fee.
Question: how much is the principal (actual amount sent) and how much is the handling fee?

The procedure says: Place the total amount of money. Below it, place one guan (1000 wen), and add the handling fee of 10 wen, making the divisor.
Divide the total amount of money by this divisor to obtain the principal amount.
Subtract the principal amount from the total money to find the remainder, which is the handling fee.

Answer: the principal is *a* guan, and the handling fee is *b* guan.
"""

# 置錢數
錢數 = 2000

# 下置一貫文，又加腳十文，為法
一貫文 = 1
腳 = Fraction(10, 1000)  # Convert 10 wen to guan
法 = 一貫文 + 腳

# 除之，得正數
正數 = Fraction(錢數, 法)

# 卻減都錢餘，即腳錢
腳錢 = 錢數 - 正數

a = 正數
b = 腳錢#----- content ends here -----

"""
"""
