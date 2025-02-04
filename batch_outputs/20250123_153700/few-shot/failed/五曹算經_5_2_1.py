"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a銖 奇 b銖 。
"""

"""
Suppose there are 738 households, and together they request 27 jin and 5 liang of silk.
Question: how much does each household receive?

The procedure says: Write down 27 jin of silk. Multiply it by 16 liang, and add 5 liang, obtaining 437 liang.
Then multiply it by 24 zhu, obtaining 10,488 zhu.
Divide it by 738 households, and the result is obtained.

Answer: *a* zhu and remainder *b* zhu.
"""

from fractions import Fraction

# 絲二十七斤五两
絲_斤 = 27
絲_两 = 5

# 以十六两乘之、納五两，得四百三十七两
絲_两總 = (絲_斤 * 16) + 絲_两

# 又以二十四銖乘之，得一萬四百八十八銖
絲_銖總 = 絲_两總 * 24

# 戶數
戶數 = 738

# 以七百三十八户除之即得
每戶_銖 = Fraction(絲_銖總, 戶數)

# 答曰：a銖 奇 b銖
a = 每戶_銖.numerator // 每戶_銖.denominator  # 整數部分
b = 每戶_銖.numerator % 每戶_銖.denominator  # 餘數部分
"""
Variable 'a' has wrong value. Expected: 1421/100, Actual: 14
Variable 'b' has wrong value. Expected: 51/50, Actual: 26"""
