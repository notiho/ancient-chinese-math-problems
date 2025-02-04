"""
今有貴絲一两直錢五十六文賤絲一两直錢四十二文有錢一百三十一貫八百一十文問各得㡬何
術曰列錢一百三十一貫八百一十文為實并絲貴賤價得九十八文為法以法除實得絲一千三百四十五两以十六两除之得八十四斤餘一两次置之以三十斤除之即得
答曰各 a鈞 
"""

#----- content starts here -----
"""
Suppose there is expensive silk, one liang of which is worth 56 wen, and cheap silk, one liang of which is worth 42 wen.
There is a total of 131 guan and 810 wen.
Question: how much of each type of silk can be obtained?

The procedure says: Arrange the total money, 131 guan and 810 wen, as the dividend.
Combine the prices of expensive and cheap silk, obtaining 98 wen as the divisor.
Divide the dividend by the divisor, obtaining 1345 liang of silk.
Divide this by 16 liang to obtain 84 jin and a remainder of 1 liang.
Next, arrange this and divide by 30 jin to obtain the result.

Answer: each *a* jun.
"""

# 貴絲一两直錢五十六文
貴絲價 = 56

# 賤絲一两直錢四十二文
賤絲價 = 42

# 有錢一百三十一貫八百一十文
總錢 = 131 * 1000 + 810  # Convert guan to wen (1 guan = 1000 wen)

# 并絲貴賤價得九十八文為法
法 = 貴絲價 + 賤絲價

# 以法除實得絲一千三百四十五两
絲兩 = 總錢 // 法

# 以十六两除之得八十四斤餘一两
絲斤 = 丝两 // 16
餘兩 = 丝两 % 16

# 次置之以三十斤除之即得
a = Fraction(絲斤, 30)  # Convert jin to jun (1 jun = 30 jin)#----- content ends here -----

"""
Code error: name '丝两' is not defined"""
