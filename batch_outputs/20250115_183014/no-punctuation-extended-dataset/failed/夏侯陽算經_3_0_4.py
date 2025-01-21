"""
今有黄金一斤直絹一千二百匹問毎兩直絹幾何
術曰置絹數以一十六兩除之即得
答曰 a兩 直絹 b匹
"""

"""
Suppose there is 1 jin of gold, worth 1200 bolts of silk.
Question: how much silk is each liang of gold worth?

The procedure says: Place the number of bolts of silk, and divide it by 16 liang (since 1 jin = 16 liang). This gives the result.

Answer: each liang of gold is worth *b* bolts of silk.
"""

# 黄金一斤
金 = 1  # in jin

# 一斤 = 16兩
兩 = 16 * 金

# 絹一千二百匹
絹 = 1200

# 置絹數，以一十六兩除之
b = Fraction(絹, 兩)  # 每兩直絹 b 匹
"""
Missing variable in output: 'a'"""
