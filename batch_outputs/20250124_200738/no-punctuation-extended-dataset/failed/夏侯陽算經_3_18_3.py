"""
今有絹二千四百五十四匹每匹直錢一貫七百文問計錢幾何
術曰先置絹數七添之退位一等即得
答曰 a貫
"""

#----- content starts here -----
"""
Suppose there are 2454 bolts of silk, each bolt worth 1 guan and 700 wen.
Question: what is the total amount of money?

The procedure says: First, place the number of bolts of silk. Add 7 to it, then shift the position down by one place, and the result is obtained.

The answer says: *a* guan.
"""

# 絹二千四百五十四匹
絹數 = 2454

# 每匹直錢一貫七百文
每匹直錢 = 1 + Fraction(700, 1000)  # 1貫7百文 = 1.7貫

# 先置絹數
總錢 = 絹數 * 每匹直錢

# 七添之
總錢 += 7

# 退位一等 (即轉換為貫，直接表示為整數部分)
a = int(總錢)  # 只取整數部分，表示貫數#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 20859/5, Actual: 4178"""
