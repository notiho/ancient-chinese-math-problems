"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a銖 奇 b銖 。
"""

#----- content starts here -----
"""
Suppose there are 738 households, collectively requesting 27 jin and 5 liang of silk.
Question: how much silk does each household receive?

The procedure says: Place the silk amount as 27 jin. Multiply it by 16 liang, and add 5 liang, obtaining 437 liang.
Then multiply it by 24 zhu, obtaining 10,488 zhu.
Divide this by 738 households to obtain the result.

Answer: *a* zhu with a remainder of *b* zhu.
"""

from fractions import Fraction

# 絲二十七斤五两
絲斤 = 27
絲兩 = 5

# 以十六两乘之、納五两，得四百三十七两
絲總兩 = (絲斤 * 16) + 絲兩

# 又以二十四銖乘之，得一萬四百八十八銖
絲總銖 = 絲總兩 * 24

# 戶數
戶數 = 738

# 以七百三十八户除之即得
每戶銖 = Fraction(絲總銖, 戶數)

# 答曰：a銖 奇 b銖
a = 每戶銖.numerator // 每戶銖.denominator  # 商 (整數部分)
b = 每戶銖.numerator % 每戶銖.denominator  # 餘數 (剩餘銖)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1421/100, Actual: 14
Variable 'b' has wrong value. Expected: 51/50, Actual: 26"""
