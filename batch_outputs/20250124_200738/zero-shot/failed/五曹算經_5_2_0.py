"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a銖 奇 b銖 。
"""

"""
To solve this problem, we need to calculate how much silk (in "銖") each household gets. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Total silk in "斤" and "两"
silk_jin = 27
silk_liang = 5

# Convert "斤" and "两" to "两"
total_liang = silk_jin * 16 + silk_liang  # 1 斤 = 16 两

# Convert "两" to "銖"
total_zhu = total_liang * 24  # 1 两 = 24 銖

# Number of households
households = 738

# Silk per household in "銖"
silk_per_household = Fraction(total_zhu, households)

# Extract the integer part (a) and the remainder (b)
a = silk_per_household.numerator // silk_per_household.denominator
b = silk_per_household.numerator % silk_per_household.denominator

# Convert the remainder to a fraction
b = Fraction(b, silk_per_household.denominator)

# Results
a, b
#----- content ends here -----


"""


This code calculates the values of `a` (the integer part of silk in "銖" each household gets) and `b` (the fractional remainder in "銖").
"""


"""
Variable 'a' has wrong value. Expected: 1421/100, Actual: 14
Variable 'b' has wrong value. Expected: 51/50, Actual: 26/123"""
