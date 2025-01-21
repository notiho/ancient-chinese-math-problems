"""
今有黄金一斤直絹一千二百匹問毎兩直絹幾何
術曰置絹數以一十六兩除之即得
答曰 a兩 直絹 b匹
"""

"""
Suppose there is 1 jin of gold, worth 1200 bolts of silk.
Question: how many bolts of silk is each liang of gold worth?

The procedure says: Place the number of bolts of silk, and divide it by 16 liang (1 jin = 16 liang). This gives the result.

Answer: *a* liang of gold is worth *b* bolts of silk.
"""

# 黄金一斤 = 16兩
金兩 = 16

# 絹一千二百匹
絹匹 = 1200

# 置絹數，以一十六兩除之，即得
b = Fraction(絹匹, 金兩)

# 每兩直絹 b 匹
a = 1  # 每 1 兩 corresponds to b 匹
"""
"""
