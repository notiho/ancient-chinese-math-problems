"""
今有絹二千四百五十四匹每匹直錢一貫七百文問計錢幾何
術曰先置絹數七添之退位一等即得
答曰 a貫
"""

"""
Suppose there are 2454 bolts of silk, each bolt worth 1 guan and 700 wen.
Question: what is the total amount of money?

The procedure says: First, place the number of bolts of silk. Add 7 to it, then shift the position down by one place (i.e., divide by 10). This gives the result.

Answer: *a* guan.
"""

# 絹二千四百五十四匹
絹數 = 2454

# 每匹直錢一貫七百文
每匹價值 = 1 + Fraction(700, 1000)  # 1貫7百文 = 1.7貫

# 計算總價值
總價值 = 絹數 * 每匹價值

# 先置絹數，七添之
總價值_加七 = 總價值 + 7

# 退位一等，即除以10
a = Fraction(總價值_加七, 10)
"""
Variable 'a' has wrong value. Expected: 20859/5, Actual: 10447/25"""
