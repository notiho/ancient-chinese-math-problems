"""
今有絹四十二匹毎匹當錢四貫三百六十六文四分七氂八毫九絲四忽問錢幾何
術曰先置絹匹之價以七六因之即得
答曰 a貫
"""

"""
Suppose there are 42 bolts of silk, each bolt worth 4 guan, 366 wen, 4 fen, 7 li, 8 hao, 9 si, and 4 hu.
Question: how much money is the total worth?

The procedure says: First place the price of one bolt of silk.
Multiply it by 42, and the result is obtained.

Answer: *a* guan.
"""

from fractions import Fraction

# 每匹絹的價值
價值每匹 = (
    4  # 貫
    + Fraction(366, 1000)  # 文
    + Fraction(4, 10000)  # 分
    + Fraction(7, 100000)  # 氂
    + Fraction(8, 1000000)  # 毫
    + Fraction(9, 10000000)  # 絲
    + Fraction(4, 100000000)  # 忽
)

# 絹的總匹數
絹匹數 = 42

# 總價值
總價值 = 絹匹數 * 價值每匹

# 答案
a = 總價值  # 單位為貫
"""
"""
