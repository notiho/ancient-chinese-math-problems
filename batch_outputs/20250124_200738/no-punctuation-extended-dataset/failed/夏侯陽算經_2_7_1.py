"""
今有縣令毎月課料七貫三百六十一文五分二氂尋即交承舊官任六日新官任二十四日問新舊官各得幾何
術曰置錢數以三十日為法除之得一日之錢二百四十五文三分八氂四毫六因之得舊官數又四因之得新官數
答曰舊官得 a貫 新官得 b貫
"""

#----- content starts here -----
"""
Suppose a county magistrate is assigned a monthly salary of 7 guan, 361 wen, 5 fen, and 2 li. 
The outgoing official serves for 6 days, and the incoming official serves for 24 days.
Question: how much does each official receive?

The procedure says: Place the total amount of money and divide it by 30 days (the divisor), obtaining the daily salary: 245 wen, 3 fen, 8 li, and 4 hao, 6 si.
Multiply this by 6 to obtain the outgoing official's amount, and multiply it by 24 to obtain the incoming official's amount.

Answer: the outgoing official receives *a* guan, and the incoming official receives *b* guan.
"""

from fractions import Fraction

# 每月課料
月課貫 = 7
月課文 = 361
月課分 = 5
月課氂 = 2

# 將所有單位轉換為文 (1 貫 = 1000 文, 1 文 = 10 分, 1 分 = 10 氂)
總錢數 = (月課貫 * 1000) + 月課文 + (月課分 / 10) + (月課氂 / 100)

# 每月 30 日為法
法 = 30

# 除之，得一日之錢
一日之錢 = 總錢數 / 法

# 舊官任 6 日
舊官數 = 一日之錢 * 6

# 新官任 24 日
新官數 = 一日之錢 * 24

# 將結果轉換回貫、文、分、氂
def 轉換為貫文分氂(金額):
    貫 = int(金額 // 1000)
    餘額 = 金額 % 1000
    文 = int(餘額 // 1)
    餘額 = 餘額 % 1
    分 = int(餘額 * 10)
    餘額 = (餘額 * 10) % 1
    氂 = int(餘額 * 10)
    return Fraction(貫), Fraction(文), Fraction(分), Fraction(氂)

a貫, a文, a分, a氂 = 轉換為貫文分氂(舊官數)
b貫, b文, b分, b氂 = 轉換為貫文分氂(新官數)

a = a貫 + Fraction(a文, 1000) + Fraction(a分, 10000) + Fraction(a氂, 100000)
b = b貫 + Fraction(b文, 1000) + Fraction(b分, 10000) + Fraction(b氂, 100000)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 92019/62500, Actual: 14723/10000
Variable 'b' has wrong value. Expected: 92019/15625, Actual: 588921/100000"""
