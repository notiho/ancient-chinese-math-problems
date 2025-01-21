"""
今有貴絲一两直錢五十六文，賤絲一两直錢四十二文，有錢一百三十一貫八百一十文。問：各得㡬何？
術曰：列錢一百三十一貫八百一十文為實，并絲貴賤價得九十八文為法，以法除實得絲一千三百四十五两以十六两除之得八十四斤餘一两次置之以三十斤除之即得。
答曰：各 a(=14/5)鈞 b(=1) 两。
"""

"""
Suppose there is expensive silk, one liang of which is worth 56 wen, and cheap silk, one liang of which is worth 42 wen.
There is a total of 131 guan and 810 wen in money.
Question: how much of each type of silk can be obtained?

The procedure says: Arrange the total money, 131 guan and 810 wen, as the dividend.
Add the prices of expensive and cheap silk, obtaining 98 wen as the divisor.
Divide the dividend by the divisor, obtaining 1345 liang of silk.
Divide by 16 liang to obtain 84 jin with 1 liang remaining.
Then arrange it, and divide by 30 jin to obtain the result.

Answer: *a*(=14/5) jun and *b*(=1) liang.
"""

# 貴絲一两直錢五十六文
貴絲價 = 56

# 賤絲一两直錢四十二文
賤絲價 = 42

# 有錢一百三十一貫八百一十文
總錢 = 131 * 1000 + 810  # Convert guan to wen

# 并絲貴賤價得九十八文為法
法 = 貴絲價 + 賤絲價

# 以法除實得絲一千三百四十五两
絲總量 = Fraction(總錢, 法)  # Total silk in liang

# 以十六两除之得八十四斤餘一两
絲斤 = 丝總量 // 16  # Full jin
絲餘兩 = 丝總量 % 16  # Remaining liang

# 次置之以三十斤除之即得
a = Fraction(絲斤, 30)  # Jun (30 jin per jun)
b = 丝餘兩  # Remaining liang

# a = 14/5 jun, b = 1 liang
"""
Code error: name '丝總量' is not defined"""
