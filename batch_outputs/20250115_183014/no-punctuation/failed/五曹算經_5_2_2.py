"""
今有七百三十八户共請絲二十七斤五两問户得㡬何
術曰列絲二十七斤以十六两乘之納五两得四百三十七两又以二十四銖乘之得一萬四百八十八銖以七百三十八户除之即得
答曰 a銖 b 絫 c黍 奇 d銖 e黍 
"""

"""
Suppose there are 738 households collectively requesting 27 jin and 5 liang of silk.
Question: how much does each household receive?

The procedure says: Place the silk amount of 27 jin, multiply it by 16 liang, and add 5 liang, obtaining 437 liang.
Then multiply it by 24 zhu, obtaining 10,488 zhu.
Divide this by 738 households, obtaining the result.

The answer says: *a* zhu, *b* lü, *c* shu, remainder *d* zhu, *e* shu.
"""

# 絲二十七斤
絲斤 = 27

# 以十六两乘之
絲兩 = 16 * 絲斤

# 納五两
絲兩 += 5

# 得四百三十七两
絲總兩 = 絲兩  # 437

# 又以二十四銖乘之
絲銖 = 24 * 絲總兩

# 得一萬四百八十八銖
絲總銖 = 絲銖  # 10488

# 以七百三十八户除之
戶數 = 738
每戶銖 = Fraction(絲總銖, 戶數)

# 分解結果
a = 每戶銖.numerator // 每戶銖.denominator  # 整數部分，銖
剩餘銖 = 每戶銖 - a  # 餘數部分

# 餘數部分轉換為黍
銖轉黍 = 24  # 1 銖 = 24 黍
b = 剩餘銖.numerator * 銖轉黍 // 剩餘銖.denominator  # 絫部分，黍
剩餘黍 = 剩餘銖 - Fraction(b, 銖轉黍)

# 餘數部分再細分
c = 剩餘黍.numerator  # 奇部分，黍

# 餘數再分解為銖和黍
d = 剩餘黍.numerator // 剩餘黍.denominator  # 餘數部分，銖
e = 剩餘黍.numerator % 剩餘黍.denominator  # 餘數部分，黍
"""
Variable 'b' has wrong value. Expected: 2, Actual: 5
Variable 'd' has wrong value. Expected: 1, Actual: 0
Variable 'e' has wrong value. Expected: 2, Actual: 1"""
