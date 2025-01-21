"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a銖 b 絫 c黍 奇 d銖 e黍 。
"""

"""
Suppose there are 738 households collectively requesting 27 jin and 5 liang of silk.
Question: how much does each household receive?

The procedure says: Place the silk amount as 27 jin. Multiply it by 16 liang, and add 5 liang, obtaining 437 liang.
Then multiply it by 24 zhu, obtaining 10,488 zhu.
Divide this by 738 households to obtain the result.

Answer: *a* zhu, *b* lü, *c* shu, remainder *d* zhu, *e* shu.
"""

from fractions import Fraction

# 絲二十七斤五两
絲_斤 = 27
絲_两 = 5

# 以十六两乘之、納五两，得四百三十七两
絲_两 = (絲_斤 * 16) + 絲_两

# 又以二十四銖乘之，得一萬四百八十八銖
絲_銖 = 絲_两 * 24

# 以七百三十八户除之即得
戶數 = 738
戶得_銖 = Fraction(絲_銖, 戶數)

# 將銖轉換為銖、絫、黍
# 1 絫 = 24 黍
# 1 銖 = 24 絫

a = 戶得_銖.numerator // 戶得_銖.denom
"""
Code error: 'Fraction' object has no attribute 'denom'"""
