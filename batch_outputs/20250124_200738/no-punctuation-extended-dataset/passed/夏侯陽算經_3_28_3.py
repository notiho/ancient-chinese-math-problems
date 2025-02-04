"""
今有絹四十二匹毎匹當錢四貫三百六十六文四分七氂八毫九絲四忽問錢幾何
術曰先置絹匹之價以七六因之即得
答曰 a貫
"""

#----- content starts here -----
"""
Suppose there are 42 bolts of silk, each bolt worth 4 guan, 366 wen, 4 fen, 7 li, 8 hao, 9 si, and 4 hu.
Question: how much money in total?

The procedure says: First, place the price of one bolt of silk. Multiply it by 42, and the result is obtained.

Answer: *a* guan.
"""

from fractions import Fraction

# 絹四十二匹
絹匹數 = 42

# 每匹當錢四貫三百六十六文四分七氂八毫九絲四忽
價值_貫 = 4
價值_文 = 366
價值_分 = Fraction(4, 10)  # 1 分 = 1/10 文
價值_氂 = Fraction(7, 100)  # 1 氂 = 1/100 文
價值_毫 = Fraction(8, 1000)  # 1 毫 = 1/1000 文
價值_絲 = Fraction(9, 10000)  # 1 絲 = 1/10000 文
價值_忽 = Fraction(4, 100000)  # 1 忽 = 1/100000 文

# 計算每匹的總價值（以貫為單位）
每匹價值 = (
    價值_貫
    + Fraction(價值_文, 1000)  # 1 貫 = 1000 文
    + Fraction(價值_分, 1000)
    + Fraction(價值_氂, 1000)
    + Fraction(價值_毫, 1000)
    + Fraction(價值_絲, 1000)
    + Fraction(價值_忽, 1000)
)

# 以七六因之，即得
總價值 = 絹匹數 * 每匹價值

a = 總價值
#----- content ends here -----

"""
"""
