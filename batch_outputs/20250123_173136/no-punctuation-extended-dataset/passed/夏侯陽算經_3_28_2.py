"""
今有絹四十二匹毎匹當錢四貫三百六十六文四分七氂八毫九絲四忽問錢幾何
術曰先置絹匹之價以七六因之即得
答曰 a貫
"""

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
價值每匹 = (
    4  # 貫
    + Fraction(366, 1000)  # 文 (1貫 = 1000文)
    + Fraction(4, 10000)  # 分 (1文 = 10分)
    + Fraction(7, 100000)  # 氂 (1分 = 10氂)
    + Fraction(8, 1000000)  # 毫 (1氂 = 10毫)
    + Fraction(9, 10000000)  # 絲 (1毫 = 10絲)
    + Fraction(4, 100000000)  # 忽 (1絲 = 10忽)
)

# 以七六因之，即得
總價值 = 絹匹數 * 價值每匹

# 答曰 a貫
a = 總價值
"""
"""
