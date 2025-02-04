"""
今有絹二千四百五十四匹每匹直錢一貫七百文問計錢幾何
術曰先置絹數七添之退位一等即得
答曰 a貫
"""

#----- content starts here -----
"""
Suppose there are 2454 bolts of silk, each bolt worth 1 guan and 700 wen.
Question: what is the total value in qian?

The procedure says: First, place the number of bolts of silk.
Add 7 to it, then shift one place to the left (multiply by 10).
This gives the total value in guan.

Answer: *a* guan.
"""

# 絹二千四百五十四匹
絹數 = 2454

# 每匹直錢一貫七百文
每匹價值_貫 = 1
每匹價值_文 = 700

# 先置絹數
總絹數 = 絹數

# 七添之
總絹數 += 7

# 退位一等 (shift one place to the left, i.e., multiply by 10)
總價值_貫 = 總絹數 * 10

a = 總價值_貫#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 20859/5, Actual: 24610"""
