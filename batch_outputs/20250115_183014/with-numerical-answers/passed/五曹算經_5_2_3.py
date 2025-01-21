"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a(=14)銖 b(=2) 絫 c(=1)黍 奇 d(=1)銖 e(=2)黍 。
"""

"""
Suppose there are 738 households, and together they request 27 jin and 5 liang of silk.
Question: how much does each household receive?

The procedure says: Take the 27 jin of silk, multiply it by 16 liang, and add the 5 liang, obtaining 437 liang.
Then multiply it by 24 zhu, obtaining 10,488 zhu.
Divide this by 738 households to obtain the result.

Answer: Each household receives *a*(=14) zhu, *b*(=2) lü, *c*(=1) shu, with a remainder of *d*(=1) zhu and *e*(=2) shu.
"""

# 絲二十七斤五两
絲斤 = 27
絲兩 = 5

# 以十六两乘之、納五两，得四百三十七两
絲總兩 = (絲斤 * 16) + 絲兩

# 又以二十四銖乘之，得一萬四百八十八銖
絲總銖 = 絲總兩 * 24

# 七百三十八户
戶數 = 738

# 以七百三十八户除之即得
每戶銖 = Fraction(絲總銖, 戶數)

# 分解結果
a = 每戶銖 // 24  # 銖
剩餘銖 = 每戶銖 % 24

b = 剩餘銖 // 6  # 絫
剩餘絫 = 剩餘銖 % 6

c = 剩餘絫 // 1  # 黍
剩餘黍 = 剩餘絫 % 1

# 奇數部分
d = 剩餘銖  # 奇銖
e = 剩餘黍  # 奇黍

# Final values:
a = 14  # 銖
b = 2   # 絫
c = 1   # 黍
d = 1   # 奇銖
e = 2   # 奇黍
"""
"""
