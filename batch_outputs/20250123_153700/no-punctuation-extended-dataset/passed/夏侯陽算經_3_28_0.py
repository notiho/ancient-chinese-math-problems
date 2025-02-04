"""
今有絹四十二匹毎匹當錢四貫三百六十六文四分七氂八毫九絲四忽問錢幾何
術曰先置絹匹之價以七六因之即得
答曰 a貫
"""

"""
Suppose there are 42 bolts of silk, each valued at 4 guan, 366 wen, 4 fen, 7 li, 8 hao, 9 si, and 4 hu.
Question: how much money in total?

The procedure says: First, place the value of one bolt of silk.
Multiply it by the number of bolts, and the result is obtained.

The answer says: *a* guan.
"""

from fractions import Fraction

# 絹四十二匹
絹匹 = 42

# 每匹當錢四貫三百六十六文四分七氂八毫九絲四忽
單價 = 4 + Fraction(366, 1000) + Fraction(4, 10000) + Fraction(7, 100000) + Fraction(8, 1000000) + Fraction(9, 10000000) + Fraction(4, 100000000)

# 以七六因之 (即以匹數乘單價)
總價 = 絹匹 * 單價

# 答曰 a貫
a = 總價
"""
"""
