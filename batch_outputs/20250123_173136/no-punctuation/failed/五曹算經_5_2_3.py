"""
今有七百三十八户共請絲二十七斤五两問户得㡬何
術曰列絲二十七斤以十六两乘之納五两得四百三十七两又以二十四銖乘之得一萬四百八十八銖以七百三十八户除之即得
答曰 a銖 奇 b銖 
"""

"""
Suppose there are 738 households collectively requesting 27 jin and 5 liang of silk.
Question: how much does each household receive?

The procedure says: Place the silk amount, 27 jin. Multiply it by 16 liang per jin, and add 5 liang, obtaining 437 liang.
Then multiply it by 24 zhu per liang, obtaining 10488 zhu.
Divide this by 738 households, and the result is the amount each household receives.

Answer: *a* zhu, remainder *b* zhu.
"""

# 絲二十七斤
絲斤 = 27

# 以十六两乘之
絲兩 = 絲斤 * 16

# 納五两
絲兩 += 5

# 得四百三十七两
絲總兩 = 絲兩  # 437 liang

# 又以二十四銖乘之
絲銖 = 絲總兩 * 24

# 得一萬四百八十八銖
絲總銖 = 絲銖  # 10488 zhu

# 以七百三十八户除之
戶數 = 738
每戶得銖 = 丝總銖 // 戶數
餘銖 = 丝總銖 % 戶數

a = 每戶得銖
b = 餘銖
"""
Code error: name '丝總銖' is not defined"""
