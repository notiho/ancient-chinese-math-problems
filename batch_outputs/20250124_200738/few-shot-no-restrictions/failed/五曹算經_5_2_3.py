"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a銖 奇 b銖 。
"""

#----- content starts here -----
"""
Suppose there are 738 households, and together they request 27 jin and 5 liang of silk.
Question: how much silk does each household receive?

The procedure says: Place the silk amount of 27 jin.
Multiply it by 16 liang per jin, and add the 5 liang, obtaining 437 liang.
Then multiply it by 24 zhu per liang, obtaining 10,488 zhu.
Divide this by 738 households to get the result.

Answer: *a* zhu and remainder *b* zhu.
"""

from fractions import Fraction

# Total silk: 27 jin and 5 liang
絲_斤 = 27
絲_兩 = 5

# Conversion factors
一斤_兩 = 16  # 1 jin = 16 liang
一兩_銖 = 24  # 1 liang = 24 zhu

# Convert silk to zhu
絲_兩總 = (絲_斤 * 一斤_兩) + 絲_兩  # Convert jin to liang and add the remaining liang
絲_銖總 = 絲_兩總 * 一兩_銖  # Convert liang to zhu

# Total households
戶數 = 738

# Divide total zhu by households
每戶_銖 = Fraction(絲_銖總, 戶數)

# Extract integer part and remainder
a = 每戶_銖.numerator // 每戶_銖.denominator  # Integer part
b = 每戶_銖.numerator % 每戶_銖.denominator  # Remainder

# Output results
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1421/100, Actual: 14
Variable 'b' has wrong value. Expected: 51/50, Actual: 26"""
