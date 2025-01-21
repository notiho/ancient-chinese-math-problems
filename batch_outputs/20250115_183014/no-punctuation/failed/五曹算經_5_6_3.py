"""
今有貴絲一两直錢五十六文賤絲一两直錢四十二文有錢一百三十一貫八百一十文問各得㡬何
術曰列錢一百三十一貫八百一十文為實并絲貴賤價得九十八文為法以法除實得絲一千三百四十五两以十六两除之得八十四斤餘一两次置之以三十斤除之即得
答曰各 a鈞 b 两
"""

"""
Suppose there is expensive silk, 1 liang of which is worth 56 wen, and cheap silk, 1 liang of which is worth 42 wen.
There is a total of 131 guan and 810 wen.
Question: how much of each type of silk is obtained?

The procedure says: Arrange the total money, 131 guan and 810 wen, as the dividend.
Add the prices of expensive and cheap silk, obtaining 98 wen as the divisor.
Divide the dividend by the divisor, obtaining 1345 liang of silk.
Divide this by 16 liang to obtain 84 jin and 1 liang remaining.
Next, arrange this and divide by 30 jin to obtain the final result.

Answer: each type of silk is *a* jun and *b* liang.
"""

# 貴絲一两直錢五十六文
貴絲價 = 56

# 賤絲一两直錢四十二文
賤絲價 = 42

# 有錢一百三十一貫八百一十文
總錢 = 131 * 1000 + 810  # 1貫 = 1000文

# 并絲貴賤價得九十八文為法
法 = 貴絲價 + 賤絲價

# 以法除實得絲一千三百四十五两
絲總量 = 總錢 // 法  # 絲總量 in 兩

# 以十六两除之得八十四斤餘一两
斤 = 丝總量 // 16  # 1斤 = 16兩
餘兩 = 丝總量 % 16

# 次置之以三十斤除之即得
a = 斤 // 30  # 1鈞 = 30斤
b = 斤 % 30  # 剩餘斤數

# 答案
a鈞 = a
b两 = 餘兩
"""
Code error: name '丝總量' is not defined"""
