"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a銖 奇 b銖 。
"""

"""
To solve this problem, we need to determine how much silk (in "銖") each household gets. Here's the Python code to compute the values of `a` (whole "銖") and `b` (remaining "銖"):


"""

#----- content starts here -----

from fractions import Fraction

# Given data
total_silk_jin = 27  # Total silk in "斤"
total_silk_liang = 5  # Additional silk in "两"
total_households = 738  # Total households

# Conversion factors
liang_to_zhu = 24  # 1 两 = 24 銖
jin_to_liang = 16  # 1 斤 = 16 两

# Convert total silk to 銖
total_silk_liang += total_silk_jin * jin_to_liang  # Convert 斤 to 两 and add
total_silk_zhu = total_silk_liang * liang_to_zhu  # Convert 两 to 銖

# Divide total 銖 by the number of households
silk_per_household = Fraction(total_silk_zhu, total_households)

# Extract whole 銖 (a) and remaining 銖 (b)
a = silk_per_household.numerator // silk_per_household.denominator
b = silk_per_household.numerator % silk_per_household.denominator

# Results
a = Fraction(a)  # Whole 銖
b = Fraction(b, silk_per_household.denominator)  # Remaining 銖 as a fraction
#----- content ends here -----


"""


### Explanation:
1. Convert the total silk into "銖" (smallest unit) using the given conversion factors.
2. Divide the total "銖" by the number of households to get the amount of silk per household.
3. Extract the whole number part (`a`) and the fractional remainder (`b`).

### Final Answer:
The variables `a` and `b` will contain the solution in terms of "銖".
"""


"""
Variable 'a' has wrong value. Expected: 1421/100, Actual: 14
Variable 'b' has wrong value. Expected: 51/50, Actual: 26/123"""
