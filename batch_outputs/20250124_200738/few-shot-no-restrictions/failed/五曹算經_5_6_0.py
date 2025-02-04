"""
今有貴絲一两直錢五十六文，賤絲一两直錢四十二文，有錢一百三十一貫八百一十文。問：各得㡬何？
術曰：列錢一百三十一貫八百一十文為實，并絲貴賤價得九十八文為法，以法除實得絲一千三百四十五两以十六两除之得八十四斤餘一两次置之以三十斤除之即得。
答曰：各 a鈞 。
"""

#----- content starts here -----
"""
Suppose there is expensive silk, where 1 liang costs 56 wen, and cheap silk, where 1 liang costs 42 wen.
There is a total of 131 guan and 810 wen.
Question: how much of each type of silk can be bought?

The procedure says: Arrange the total money, 131 guan and 810 wen, as the dividend.
Add the prices of expensive and cheap silk, obtaining 98 wen as the divisor.
Divide the dividend by the divisor, obtaining 1345 liang of silk.
Divide by 16 liang to get 84 jin and 1 liang remaining.
Then divide by 30 jin to determine the final result.

Answer: each type of silk is *a* jun.
"""

from fractions import Fraction

# 貴絲一两直錢五十六文
貴絲價 = 56  # wen per liang

# 賤絲一两直錢四十二文
賤絲價 = 42  # wen per liang

# 有錢一百三十一貫八百一十文
總錢 = 131 * 1000 + 810  # Convert guan to wen (1 guan = 1000 wen)

# 并絲貴賤價得九十八文為法
法 = 貴絲價 + 賤絲價

# 以法除實得絲一千三百四十五两
絲總量 = 總錢 // 法  # Total silk in liang

# 以十六两除之得八十四斤餘一两
斤 = 丝總量 // 16  # Convert liang to jin (16 liang = 1 jin)
餘兩 = 丝總量 % 16  # Remaining liang

# 次置之以三十斤除之即得
鈞 = 斤 // 30  # Convert jin to jun (30 jin = 1 jun)
餘斤 = 斤 % 30  # Remaining jin

a = 鈞
print(f"Each type of silk is {a} jun.")#----- content ends here -----

"""
Code error: name '丝總量' is not defined"""
