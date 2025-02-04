"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a(=1421/100)銖 奇 b(=51/50)銖 。
"""

"""
Suppose there are 738 households, and together they request 27 jin and 5 liang of silk.
Question: how much does each household receive?

The procedure says: Place the 27 jin of silk, multiply it by 16 liang, and add the 5 liang, obtaining 437 liang.
Then multiply it by 24 zhu, obtaining 10,488 zhu.
Divide by the 738 households, and the result is the amount per household.

Answer: *a*(=1421/100) zhu and *b*(=51/50) zhu remainder.
"""

from fractions import Fraction

# 絲二十七斤
絲斤 = 27

# 以十六两乘之
絲兩 = 16 * 絲斤

# 納五两
絲兩 += 5

# 得四百三十七两
總絲兩 = 絲兩  # 437

# 又以二十四銖乘之
總絲銖 = 24 * 總絲兩  # 10,488

# 七百三十八户
戶數 = 738

# 以七百三十八户除之即得
每戶銖 = Fraction(總絲銖, 戶數)  # 1421/100

# 奇數部分
a = 每戶銖  # 1421/100
b = 每戶銖 - int(每戶銖)  # 51/50
"""
Variable 'a' has wrong value. Expected: 1421/100, Actual: 1748/123
Variable 'b' has wrong value. Expected: 51/50, Actual: 26/123"""
