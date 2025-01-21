"""
今有黄金一斤直絹一千二百匹問毎兩直絹幾何
術曰置絹數以一十六兩除之即得
答曰 a兩 直絹 b匹
"""

"""
Suppose there is 1 jin of gold worth 1200 bolts of silk.
Question: how much silk is each liang of gold worth?

The procedure says: Place the number of bolts of silk and divide it by 16 liang [in 1 jin]. This gives the result.

Answer: 1 liang of gold is worth *b* bolts of silk.
"""

# 黄金一斤
黃金 = 1  # in jin

# 一斤等於十六兩
兩 = 16 * 黃金

# 絹一千二百匹
絹數 = 1200

# 置絹數以一十六兩除之即得
b = Fraction(絹數, 兩)
"""
Missing variable in output: 'a'"""
