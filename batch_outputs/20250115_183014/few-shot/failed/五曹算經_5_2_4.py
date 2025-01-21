"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a銖 b 絫 c黍 奇 d銖 e黍 。
"""

"""
Suppose there are 738 households, and together they request 27 jin and 5 liang of silk.
Question: how much does each household receive?

The procedure says: Place the silk as 27 jin. Multiply it by 16 liang, and add 5 liang, obtaining 437 liang.
Then multiply it by 24 zhu, obtaining 10,488 zhu.
Divide this by 738 households, and the result is obtained.

The answer says: *a* zhu, *b* lü, *c* shu, remainder *d* zhu, *e* shu.
"""

# 列絲二十七斤
絲斤 = 27

# 以十六两乘之
絲兩 = 16 * 絲斤

# 納五两
絲兩 += 5

# 得四百三十七两
總絲兩 = 絲兩

# 又以二十四銖乘之
總絲銖 = 24 * 總絲兩

# 得一萬四百八十八銖
總絲銖 = 10488

# 以七百三十八户除之即得
戶數 = 738
每戶銖 = Fraction(總絲銖, 戶數)

# 分解結果
a = 每戶銖.numerator // 每戶銖.denominator  # 整數部分 (銖)
剩餘銖 = 每戶銖.numerator % 每戶銖.denominator  # 餘數部分 (銖)

# 將剩餘銖轉換為黍
總黍 = 剩餘銖 * 24  # 1 銖 = 24 黍
b = 總黍 // 每戶銖.denominator  # 結果中的絫 (lü)
c = 總黍 % 每戶銖.denominator  # 結果中的黍 (shu)

# 餘數部分
d = 剩餘銖
e = c
"""
Variable 'b' has wrong value. Expected: 2, Actual: 5
Variable 'c' has wrong value. Expected: 1, Actual: 9
Variable 'd' has wrong value. Expected: 1, Actual: 26
Variable 'e' has wrong value. Expected: 2, Actual: 9"""
