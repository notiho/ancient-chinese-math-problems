"""
今有貴絲一两直錢五十六文，賤絲一两直錢四十二文，有錢一百三十一貫八百一十文。問：各得㡬何？
術曰：列錢一百三十一貫八百一十文為實，并絲貴賤價得九十八文為法，以法除實得絲一千三百四十五两以十六两除之得八十四斤餘一两次置之以三十斤除之即得。
答曰：各 a鈞 b 两。
"""

"""
Suppose there is expensive silk, 1 liang of which costs 56 wen, and cheap silk, 1 liang of which costs 42 wen. 
There is a total of 131 guan and 810 wen in money.
Question: how much silk of each type can be purchased?

The procedure says: Place the total money, 131 guan and 810 wen, as the dividend.
Add the prices of expensive and cheap silk, obtaining 98 wen as the divisor.
Divide the dividend by the divisor, obtaining 1345 liang of silk.
Divide by 16 liang to get 84 jin and 1 liang remaining.
Place the remainder and divide by 30 jin to obtain the final result.

Answer: *a* jin and *b* liang of each type.
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
總絲兩 = 總錢 // 法

# 以十六两除之得八十四斤餘一两
總絲斤 = 總絲兩 // 16
餘兩 = 總絲兩 % 16

# 次置之以三十斤除之即得
a = 總絲斤 // 2  # Each type gets half of the total jin
b = 餘兩 // 2    # Each type gets half of the remaining liang
"""
Variable 'a' has wrong value. Expected: 14/5, Actual: 42
Variable 'b' has wrong value. Expected: 1, Actual: 0"""
