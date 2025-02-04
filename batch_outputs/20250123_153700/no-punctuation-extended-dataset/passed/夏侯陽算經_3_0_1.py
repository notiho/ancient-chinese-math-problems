"""
今有黄金一斤直絹一千二百匹問毎兩直絹幾何
術曰置絹數以一十六兩除之即得
答曰一兩直絹 a匹
"""

"""
Suppose there is 1 jin of gold, worth 1200 bolts of silk.
Question: how many bolts of silk is each liang of gold worth?

The procedure says: Place the number of bolts of silk and divide it by 16 liang (1 jin = 16 liang). This gives the result.

Answer: each liang of gold is worth *a* bolts of silk.
"""

# 黄金一斤直絹一千二百匹
絹數 = 1200

# 一斤等於十六兩
每斤兩數 = 16

# 置絹數以一十六兩除之即得
a = Fraction(絹數, 每斤兩數)
"""
"""
