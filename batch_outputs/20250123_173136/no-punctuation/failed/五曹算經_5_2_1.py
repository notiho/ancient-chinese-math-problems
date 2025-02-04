"""
今有七百三十八户共請絲二十七斤五两問户得㡬何
術曰列絲二十七斤以十六两乘之納五两得四百三十七两又以二十四銖乘之得一萬四百八十八銖以七百三十八户除之即得
答曰 a銖 奇 b銖 
"""

"""
Suppose there are 738 households collectively requesting 27 jin and 5 liang of silk.
Question: how much does each household receive?

The procedure says: Write down 27 jin of silk. Multiply it by 16 liang, and add 5 liang, obtaining 437 liang.
Then multiply it by 24 zhu, obtaining 10,488 zhu.
Divide it by 738 households, and the result is the amount per household.

Answer: *a* zhu, remainder *b* zhu.
"""

from fractions import Fraction

# 絲二十七斤
絲斤 = 27

# 以十六两乘之
絲兩 = 絲斤 * 16

# 納五两
絲兩 += 5

# 得四百三十七两
總絲兩 = 絲兩  # 總絲兩 = 437

# 又以二十四銖乘之
總絲銖 = 總絲兩 * 24

# 得一萬四百八十八銖
總絲銖 = 總絲銖  # 總絲銖 = 10488

# 七百三十八户
戶數 = 738

# 以七百三十八户除之
每戶銖 = Fraction(總絲銖, 戶數)

# 整數部分
a = 每戶銖.numerator // 每戶銖.denominator

# 餘數部分
b = 每戶銖.numerator % 每戶銖.denominator
"""
Variable 'a' has wrong value. Expected: 1421/100, Actual: 14
Variable 'b' has wrong value. Expected: 51/50, Actual: 26"""
