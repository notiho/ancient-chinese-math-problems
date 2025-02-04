"""
今有七百三十八户共請絲二十七斤五两問户得㡬何
術曰列絲二十七斤以十六两乘之納五两得四百三十七两又以二十四銖乘之得一萬四百八十八銖以七百三十八户除之即得
答曰 a銖 奇 b銖 
"""

#----- content starts here -----
"""
Suppose there are 738 households collectively requesting 27 jin and 5 liang of silk.
Question: how much does each household receive?

The procedure says: Place the silk amount of 27 jin, multiply it by 16 liang, and add 5 liang, obtaining 437 liang.
Then multiply it by 24 zhu, obtaining 10,488 zhu.
Divide this by 738 households, and the result is the amount each household receives.

Answer: *a* zhu, remainder *b* zhu.
"""

from fractions import Fraction

# 絲二十七斤
絲_斤 = 27

# 以十六两乘之
絲_兩 = 16 * 絲_斤

# 納五两
絲_兩 += 5

# 以二十四銖乘之
絲_銖 = 24 * 絲_兩

# 七百三十八户
戶數 = 738

# 以七百三十八户除之
每戶_銖 = Fraction(絲_銖, 戶數)

# 整數部分
a = 每戶_銖.numerator // 每戶_銖.denominator

# 餘數部分
b = 每戶_銖.numerator % 每戶_銖.denominator#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1421/100, Actual: 14
Variable 'b' has wrong value. Expected: 51/50, Actual: 26"""
