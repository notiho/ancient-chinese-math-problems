"""
今有黄金一斤直絹一千二百匹問毎兩直絹幾何
術曰置絹數以一十六兩除之即得
答曰 a兩 直絹 b匹
"""

"""
Suppose there is 1 jin of gold, worth 1200 bolts of silk.
Question: how much silk is worth per liang of gold?

The procedure says: Place the number of bolts of silk and divide it by 16 liang (since 1 jin = 16 liang). This gives the result.

Answer: *a* liang of gold is worth *b* bolts of silk.
"""

# 黄金一斤
黃金 = 1  # in jin

# 直絹一千二百匹
絹數 = 1200

# 一斤等於十六兩
每斤兩數 = 16

# 置絹數，以一十六兩除之，即得
b = Fraction(絹數, 每斤兩數)

# 每兩直絹 b 匹
a = 1  # 每兩 represents 1 liang
"""
"""
