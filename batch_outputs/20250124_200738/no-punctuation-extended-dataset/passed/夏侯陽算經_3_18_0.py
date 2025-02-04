"""
今有絹二千四百五十四匹每匹直錢一貫七百文問計錢幾何
術曰先置絹數七添之退位一等即得
答曰 a貫
"""

#----- content starts here -----
"""
Suppose there are 2454 bolts of silk, each worth 1 guan and 700 wen.
Question: what is the total amount of money?

The procedure says: First, place the number of bolts of silk.
Add 7 to it, then shift the position down by one place (multiply by 10).
This gives the total amount.

Answer: *a* guan.
"""

# 絹二千四百五十四匹
絹數 = 2454

# 每匹直錢一貫七百文
每匹價值 = 1 + Fraction(700, 1000)  # 1貫7百文 = 1.7貫

# 計算總價值
總價值 = 絹數 * 每匹價值

# 轉換為貫
a = 總價值  # 答案以貫為單位#----- content ends here -----

"""
"""
