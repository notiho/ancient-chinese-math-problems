"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a銖 b 絫 c黍 奇 d銖 e黍 。
"""

"""
Suppose there are 738 households collectively requesting 27 jin and 5 liang of silk.
Question: how much does each household receive?

The procedure says: Write down 27 jin of silk. Multiply it by 16 liang, and add 5 liang, obtaining 437 liang.
Then, multiply it by 24 zhu, obtaining 10,488 zhu.
Divide this by 738 households to get the result.

Answer: *a* zhu, *b* lü, *c* shu, with a remainder of *d* zhu and *e* shu.
"""

# 絲二十七斤五两
絲_斤 = 27
絲_两 = 5

# 以十六两乘之、納五两，得四百三十七两
絲_两 = (絲_斤 * 16) + 絲_两

# 又以二十四銖乘之，得一萬四百八十八銖
絲_銖 = 絲_两 * 24

# 戶數
戶數 = 738

# 以七百三十八户除之即得
每戶_銖 = Fraction(絲_銖, 戶數)

# 轉換為銖、絫、黍
a = 每戶_銖 // 24  # 銖
剩餘_銖 = 每戶_銖 % 24

b = 剩餘_銖 // 1  # 絫 (1絫 = 1銖, so this is the remaining銖)
c = 剩餘_銖 % 1 * 1000  # 黍 (1銖 = 1000黍)

# 餘數部分
d = 剩餘_銖 // 1  # 餘數銖
e = 剩餘_銖 % 1 * 1000  # 餘數黍
"""
Variable 'a' has wrong value. Expected: 14, Actual: 0
Variable 'b' has wrong value. Expected: 2, Actual: 14
Variable 'c' has wrong value. Expected: 1, Actual: 26000/123
Variable 'd' has wrong value. Expected: 1, Actual: 14
Variable 'e' has wrong value. Expected: 2, Actual: 26000/123"""
