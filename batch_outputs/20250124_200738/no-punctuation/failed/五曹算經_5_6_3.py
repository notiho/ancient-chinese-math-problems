"""
今有貴絲一两直錢五十六文賤絲一两直錢四十二文有錢一百三十一貫八百一十文問各得㡬何
術曰列錢一百三十一貫八百一十文為實并絲貴賤價得九十八文為法以法除實得絲一千三百四十五两以十六两除之得八十四斤餘一两次置之以三十斤除之即得
答曰各 a鈞 
"""

#----- content starts here -----
"""
Suppose there is expensive silk, one liang of which is worth 56 wen, and cheap silk, one liang of which is worth 42 wen.
There is 131 guan and 810 wen of money.
Question: how much of each type of silk can be obtained?

The procedure says: Place the money, 131 guan and 810 wen, as the dividend.
Combine the prices of expensive and cheap silk, obtaining 98 wen as the divisor.
Divide the dividend by the divisor, obtaining 1345 liang of silk.
Divide by 16 liang to obtain 84 jin with 1 liang remaining.
Next, place it and divide by 30 jin to obtain the result.

Answer: each type of silk is *a* jun.
"""

# 貴絲一两直錢五十六文
貴絲價 = 56

# 賤絲一两直錢四十二文
賤絲價 = 42

# 有錢一百三十一貫八百一十文
錢 = 131 * 1000 + 810  # Convert guan to wen

# 并絲貴賤價得九十八文，為法
法 = 貴絲價 + 賤絲價

# 以法除實，得絲一千三百四十五两
絲兩 = 錢 // 法

# 以十六两除之，得八十四斤餘一两
斤 = 丝两 // 16
餘兩 = 丝两 % 16

# 次置之，以三十斤除之，即得
a = 斤 // 30  # Each type of silk in jun
#----- content ends here -----

"""
Code error: name '丝两' is not defined"""
