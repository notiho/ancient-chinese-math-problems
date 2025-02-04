"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a銖 奇 b銖 。
"""

#----- content starts here -----
"""
Suppose there are 738 households, and together they request 27 jin and 5 liang of silk.
Question: how much silk does each household receive?

The procedure says: Place the 27 jin of silk, multiply it by 16 liang, and add the 5 liang, obtaining 437 liang.
Then multiply it by 24 zhu, obtaining 10,488 zhu.
Divide this by the 738 households to get the result.

Answer: Each household gets *a* zhu and a remainder of *b* zhu.
"""

from fractions import Fraction

# Total silk: 27 jin and 5 liang
jin = 27
liang = 5

# Conversion factors
liang_per_jin = 16  # 1 jin = 16 liang
zhu_per_liang = 24  # 1 liang = 24 zhu

# Total households
households = 738

# Convert jin and liang to total zhu
total_liang = jin * liang_per_jin + liang  # Convert jin to liang and add the remaining liang
total_zhu = total_liang * zhu_per_liang   # Convert liang to zhu

# Divide total zhu by the number of households
zhu_per_household = Fraction(total_zhu, households)

# Extract the integer part (a) and the remainder (b)
a = zhu_per_household.numerator // zhu_per_household.denominator  # Integer part
b = zhu_per_household.numerator % zhu_per_household.denominator  # Remainder

# Final result
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1421/100, Actual: 14
Variable 'b' has wrong value. Expected: 51/50, Actual: 26"""
