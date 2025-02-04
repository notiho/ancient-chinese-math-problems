"""
今有七百三十八户共請絲二十七斤五两問户得㡬何
術曰列絲二十七斤以十六两乘之納五两得四百三十七两又以二十四銖乘之得一萬四百八十八銖以七百三十八户除之即得
答曰 a銖 奇 b銖 
"""

"""
Suppose there are 738 households collectively requesting 27 jin and 5 liang of silk.
Question: how much does each household receive?

The procedure says: Place the silk amount of 27 jin. Multiply it by 16 liang, then add 5 liang, obtaining 437 liang.
Then multiply by 24 zhu, obtaining 10,488 zhu.
Divide by 738 households, and the result is obtained.

Answer: *a* zhu, remainder *b* zhu.
"""

from fractions import Fraction

# 絲二十七斤
絲_斤 = 27

# 以十六两乘之
絲_两 = 16 * 絲_斤

# 納五两
絲_两 += 5

# 得四百三十七两
絲_总两 = 絲_两

# 又以二十四銖乘之
絲_銖 = 24 * 絲_总两

# 得一萬四百八十八銖
絲_总銖 = 絲_銖

# 以七百三十八户除之
戶數 = 738
每戶_銖 = Fraction(絲_总銖, 戶數)

# 整數部分
a = 每戶_銖.numerator // 每戶_銖.denominator

# 餘數部分
b = 每戶_銖.numerator % 每戶_銖.denominator
"""
Variable 'a' has wrong value. Expected: 1421/100, Actual: 14
Variable 'b' has wrong value. Expected: 51/50, Actual: 26"""
