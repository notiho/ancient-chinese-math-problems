"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a(=14)銖 b(=2) 絫 c(=1)黍 奇 d(=1)銖 e(=2)黍 。
"""

"""
Suppose there are 738 households, and they collectively request 27 jin and 5 liang of silk.
Question: how much does each household receive?

The procedure says: Write down 27 jin of silk. Multiply it by 16 liang and add 5 liang, obtaining 437 liang.
Then multiply it by 24 zhu, obtaining 10488 zhu.
Divide this by 738 households to obtain the result.

Answer: Each household receives *a*(=14) zhu, *b*(=2) lü, *c*(=1) shu, with a remainder of *d*(=1) zhu and *e*(=2) shu.
"""

# 絲二十七斤五两
絲斤 = 27
絲兩 = 5

# 以十六两乘之、納五两，得四百三十七两
絲兩總 = (絲斤 * 16) + 絲兩  # 437

# 又以二十四銖乘之，得一萬四百八十八銖
絲銖總 = 絲兩總 * 24  # 10488

# 以七百三十八户除之即得
戶數 = 738
每戶銖 = Fraction(絲銖總, 戶數)  # Fraction(10488, 738)

# 分解結果
a = 每戶銖 // 24  # 14銖
剩餘銖 = 每戶銖 % 24

b = 剩餘銖 // 4  # 2絫
剩餘絫 = 剩餘銖 % 4

c = 剩餘絫 // 1  # 1黍
剩餘黍 = 剩餘絫 % 1

# 奇數部分
d = 剩餘銖  # 1銖
e = 剩餘黍 * 4  # 2黍
"""
Variable 'a' has wrong value. Expected: 14, Actual: 0
Variable 'b' has wrong value. Expected: 2, Actual: 3
Variable 'c' has wrong value. Expected: 1, Actual: 2
Variable 'd' has wrong value. Expected: 1, Actual: 1748/123
Variable 'e' has wrong value. Expected: 2, Actual: 104/123"""
