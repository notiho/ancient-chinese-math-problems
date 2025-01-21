"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a(=14)銖 b(=2) 絫 c(=1)黍 奇 d(=1)銖 e(=2)黍 。
"""

"""
Suppose there are 738 households collectively requesting 27 jin and 5 liang of silk.
Question: how much does each household receive?

The procedure says: Place the silk amount as 27 jin. Multiply it by 16 liang per jin, and add the 5 liang, obtaining 437 liang.
Then multiply by 24 zhu per liang, obtaining 10488 zhu.
Divide by 738 households to get the result.

Answer: Each household receives *a*(=14) zhu, *b*(=2) lü, *c*(=1) shu, with a remainder of *d*(=1) zhu and *e*(=2) shu.
"""

# 列絲二十七斤，以十六两乘之、納五两
絲斤 = 27
絲兩 = 5
總兩 = (絲斤 * 16) + 絲兩  # 437兩

# 又以二十四銖乘之
銖每兩 = 24
總銖 = 總兩 * 銖每兩  # 10488銖

# 以七百三十八户除之即得
戶數 = 738
每戶銖 = Fraction(總銖, 戶數)  # 10488 / 738 = 14 + 2/738

# 轉換為銖、絫、黍
a = 每戶銖 // 24  # 每戶的整銖數 (14銖)
剩餘銖 = 每戶銖 % 24

b = 剩餘銖 // 12  # 每戶的整絫數 (2絫)
剩餘絫 = 剩餘銖 % 12

c = 剩餘絫 // 4  # 每戶的整黍數 (1黍)
剩餘黍 = 剩餘絫 % 4

d = 剩餘黍  # 剩餘銖 (1銖)
e = 剩餘黍 * 2  # 剩餘黍 (2黍)
"""
Variable 'a' has wrong value. Expected: 14, Actual: 0
Variable 'b' has wrong value. Expected: 2, Actual: 1
Variable 'c' has wrong value. Expected: 1, Actual: 0
Variable 'd' has wrong value. Expected: 1, Actual: 272/123
Variable 'e' has wrong value. Expected: 2, Actual: 544/123"""
