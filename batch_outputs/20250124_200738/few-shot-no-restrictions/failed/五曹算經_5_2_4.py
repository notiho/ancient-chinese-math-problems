"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a銖 奇 b銖 。
"""

#----- content starts here -----
"""
Suppose there are 738 households, and together they request 27 jin and 5 liang of silk.
Question: how much silk does each household receive?

The procedure says: Write down the silk as 27 jin. Multiply it by 16 liang per jin, and add the 5 liang, obtaining 437 liang.
Then multiply it by 24 zhu per liang, obtaining 10,488 zhu.
Divide this by 738 households to get the result.

Answer: *a* zhu and remainder *b* zhu.
"""

from fractions import Fraction

# Total silk: 27 jin and 5 liang
jin = 27
liang = 5

# Conversion factors
liang_per_jin = 16
zhu_per_liang = 24

# Total households
households = 738

# Convert jin and liang to total liang
total_liang = (jin * liang_per_jin) + liang

# Convert total liang to total zhu
total_zhu = total_liang * zhu_per_liang

# Divide total zhu by the number of households
zhu_per_household = Fraction(total_zhu, households)

# Extract the integer part (a) and the remainder (b)
a = zhu_per_household.numerator // zhu_per_household.denominator
b = zhu_per_household.numerator % zhu_per_household.denominator

a, b  # Output the result as a zhu and remainder b zhu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1421/100, Actual: 14
Variable 'b' has wrong value. Expected: 51/50, Actual: 26"""
