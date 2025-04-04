"""
今有縣令毎月課料七貫三百六十一文五分二氂尋即交承舊官任六日新官任二十四日問新舊官各得幾何
術曰置錢數以三十日為法除之得一日之錢二百四十五文三分八氂四毫六因之得舊官數又四因之得新官數
答曰舊官得 a貫 新官得 b貫
"""

#----- content starts here -----
"""
Suppose a county magistrate is assigned a monthly salary of 7 guan, 361 wen, 5 fen, and 2 li.
The outgoing official served for 6 days, and the incoming official served for 24 days.
Question: how much does each official receive?

The procedure says: Place the total amount of money and take 30 days as the divisor.
Divide by this to obtain the daily amount of money: 245 wen, 3 fen, 8 li, 4 hao, and 6 si.
Multiply this by 6 to obtain the outgoing official's amount.
Multiply this by 24 to obtain the incoming official's amount.

Answer: the outgoing official receives *a* guan, and the incoming official receives *b* guan.
"""

from fractions import Fraction

# 每月課料
月錢_貫 = 7
月錢_文 = 361
月錢_分 = 5
月錢_氂 = 2

# 將所有單位轉換為文 (1 貫 = 1000 文, 1 文 = 10 分, 1 分 = 10 氂)
月錢_總文 = (月錢_貫 * 1000) + 月錢_文 + Fraction(月錢_分, 10) + Fraction(月錢_氂, 100)

# 每月 30 日為法
月日數 = 30

# 求一日之錢
一日錢 = 月錢_總文 / 月日數

# 舊官任 6 日
舊官錢 = 一日錢 * 6

# 新官任 24 日
新官錢 = 一日錢 * 24

# 將結果轉換回貫的格式
a = Fraction(舊官錢, 1000)  # 舊官所得貫
b = Fraction(新官錢, 1000)  # 新官所得貫#----- content ends here -----

"""
"""
