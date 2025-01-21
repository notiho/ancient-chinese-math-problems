"""
今有七百三十八户共請絲二十七斤五两問户得㡬何
術曰列絲二十七斤以十六两乘之納五两得四百三十七两又以二十四銖乘之得一萬四百八十八銖以七百三十八户除之即得
答曰 a銖 b 絫 c黍 奇 d銖 e黍 
"""

"""
Suppose there are 738 households collectively requesting 27 jin and 5 liang of silk.
Question: how much does each household receive?

The procedure says: Write down the silk as 27 jin. Multiply it by 16 liang and add the 5 liang, obtaining 437 liang.
Then multiply it by 24 zhu, obtaining 10488 zhu.
Divide this by 738 households, obtaining the result.

The answer says: *a* zhu, *b* lü, *c* shu, remainder *d* zhu, *e* shu.
"""

# 絲二十七斤
絲斤 = 27

# 以十六两乘之
絲兩 = 絲斤 * 16

# 納五两
絲兩 += 5

# 得四百三十七两
絲總兩 = 絲兩  # 437兩

# 又以二十四銖乘之
絲銖 = 絲總兩 * 24

# 得一萬四百八十八銖
絲總銖 = 絲銖  # 10488銖

# 七百三十八户
戶數 = 738

# 以七百三十八户除之
每戶銖 = Fraction(絲總銖, 戶數)

# 計算 a銖 b絫 c黍
a = 每戶銖.numerator // 每戶銖.denominator  # 整數部分為 a銖
剩餘銖 = 每戶銖.numerator % 每戶銖.denominator  # 餘數部分

# 1銖 = 10絫
b = 剩餘銖 * 10 // 每戶銖.denominator  # 計算 b絫
剩餘絫 = 剩餘銖 * 10 % 每戶銖.denominator

# 1絫 = 10黍
c = 剩餘絫 * 10 // 每戶銖.denominator  # 計算 c黍
剩餘黍 = 剩餘絫 * 10 % 每戶銖.denominator

# 奇 d銖 e黍
d = 剩餘黍 // 10  # 奇數部分為 d銖
e = 剩餘黍 % 10  # 剩餘部分為 e黍
"""
Variable 'e' has wrong value. Expected: 2, Actual: 7"""
