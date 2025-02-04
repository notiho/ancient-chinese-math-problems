"""
今有貴絲一两直錢五十六文，賤絲一两直錢四十二文，有錢一百三十一貫八百一十文。問：各得㡬何？
術曰：列錢一百三十一貫八百一十文為實，并絲貴賤價得九十八文為法，以法除實得絲一千三百四十五两以十六两除之得八十四斤餘一两次置之以三十斤除之即得。
答曰：各 a(=269/96)鈞 。
"""

"""
Suppose there is expensive silk, one liang of which is worth 56 wen, and cheap silk, one liang of which is worth 42 wen.
There is a total of 131 guan and 810 wen in money.
Question: how much of each type of silk can be obtained?

The procedure says: Arrange the total money, 131 guan and 810 wen, as the dividend.
Add the prices of the expensive and cheap silk, obtaining 98 wen as the divisor.
Divide the dividend by the divisor, obtaining 1345 liang of silk.
Divide this by 16 liang to obtain 84 jin with a remainder of 1 liang.
Place this remainder and divide by 30 jin to obtain the result.

Answer: each type of silk is *a*(=269/96) jun.
"""

from fractions import Fraction

# 貴絲一两直錢五十六文
貴絲價 = 56

# 賤絲一两直錢四十二文
賤絲價 = 42

# 有錢一百三十一貫八百一十文
總錢 = 131 * 1000 + 810  # 1貫 = 1000文

# 并絲貴賤價得九十八文為法
法 = 貴絲價 + 賤絲價  # 98文

# 以法除實得絲一千三百四十五两
絲總量 = Fraction(總錢, 法)  # 1345兩

# 以十六两除之得八十四斤餘一两
斤 = 丝總量 // 16  # 84斤
餘兩 = 丝總量 % 16  # 1兩

# 次置之以三十斤除之即得
a = Fraction(斤 * 16 + 餘兩, 30 * 16)  # 269/96鈞
"""
Code error: name '丝總量' is not defined"""
