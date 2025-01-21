"""
今有七百三十八户共請絲二十七斤五两問户得㡬何
術曰列絲二十七斤以十六两乘之納五两得四百三十七两又以二十四銖乘之得一萬四百八十八銖以七百三十八户除之即得
答曰 a銖 b 絫 c黍 奇 d銖 e黍 
"""

"""
Suppose there are 738 households collectively requesting 27 jin and 5 liang of silk.
Question: how much does each household receive?

The procedure says: Write down 27 jin of silk. Multiply it by 16 liang, then add 5 liang, obtaining 437 liang.
Then multiply it by 24 zhu, obtaining 10,488 zhu.
Divide this by 738 households, and the result is obtained.

Answer: *a* zhu, *b* lü, *c* shu, remainder *d* zhu, *e* shu.
"""

# 絲二十七斤
絲斤 = 27

# 以十六两乘之
絲兩 = 絲斤 * 16

# 納五两
絲兩 += 5

# 得四百三十七两
絲總兩 = 絲兩

# 又以二十四銖乘之
絲銖 = 絲總兩 * 24

# 得一萬四百八十八銖
絲總銖 = 絲銖

# 七百三十八户
戶數 = 738

# 以七百三十八户除之
每戶銖 = Fraction(絲總銖, 戶數)

# 分解結果
a = 每戶銖.numerator // 每戶銖.denominator  # 得到整數部分的銖數
剩餘銖 = 每戶銖.numerator % 每戶銖.denominator  # 剩餘的銖數

# 銖轉換為黍 (1 銖 = 24 黍)
剩餘黍 = Fraction(剩餘銖 * 24, 每戶銖.denominator)

b = 剩餘黍.numerator // 剩餘黍.denominator  # 得到整數部分的黍數
c = 剩餘黍.numerator % 剩餘黍.denominator  # 剩餘的黍數

# 餘數部分
d = 剩餘銖
e = c
"""
Variable 'b' has wrong value. Expected: 2, Actual: 5
Variable 'c' has wrong value. Expected: 1, Actual: 3
Variable 'd' has wrong value. Expected: 1, Actual: 26
Variable 'e' has wrong value. Expected: 2, Actual: 3"""
