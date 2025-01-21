"""
今有縣令毎月課料七貫三百六十一文五分二氂尋即交承舊官任六日新官任二十四日問新舊官各得幾何
術曰置錢數以三十日為法除之得一日之錢二百四十五文三分八氂四毫六因之得舊官數又四因之得新官數
答曰舊官得 a貫 新官得 b貫
"""

"""
Suppose a county magistrate is assigned a monthly salary of 7 guan, 361 wen, 5 fen, and 2 li.
The outgoing magistrate serves for 6 days, and the incoming magistrate serves for 24 days.
Question: how much does each magistrate receive?

The procedure says: Place the total amount of money and use 30 days as the divisor.
Divide it to obtain the amount of money for one day: 245 wen, 3 fen, 8 li, and 4 hao, 6 si.
Multiply this by 6 to obtain the outgoing magistrate's amount.
Multiply this by 24 to obtain the incoming magistrate's amount.

Answer: the outgoing magistrate receives *a* guan, and the incoming magistrate receives *b* guan.
"""

from fractions import Fraction

# 每月課料七貫三百六十一文五分二氂
月錢_貫 = 7
月錢_文 = 361
月錢_分 = Fraction(5, 10)  # 1 分 = 1/10 文
月錢_氂 = Fraction(2, 100)  # 1 氂 = 1/100 文

# 將所有單位統一為文
月錢_總文 = (月錢_貫 * 1000) + 月錢_文 + 月錢_分 + 月錢_氂

# 以三十日為法
法 = 30

# 除之，得一日之錢
一日之錢 = 月錢_總文 / 法

# 舊官任六日
舊官日數 = 6
舊官錢 = 一日之錢 * 舊官日數

# 新官任二十四日
新官日數 = 24
新官錢 = 一日之錢 * 新官日數

# 將錢轉換回貫的單位
a = Fraction(舊官錢, 1000)  # 舊官得 a 貫
b = Fraction(新官錢, 1000)  # 新官得 b 貫
"""
"""
