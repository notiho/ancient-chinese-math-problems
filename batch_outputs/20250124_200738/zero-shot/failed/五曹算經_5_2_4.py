"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a銖 奇 b銖 。
"""

"""
To solve this problem, we need to calculate how much silk (in "銖") each household gets. Here's the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
total_households = 738  # Total households
total_silk_jin = 27  # Total silk in "斤"
total_silk_liang = 5  # Additional silk in "两"

# Convert the total silk to "銖"
# 1 斤 = 16 两, 1 两 = 24 銖
total_silk_liang += total_silk_jin * 16  # Convert "斤" to "两"
total_silk_zhu = total_silk_liang * 24  # Convert "两" to "銖"

# Divide the total silk in "銖" by the number of households
silk_per_household = Fraction(total_silk_zhu, total_households)

# Extract the integer part (a) and the remainder (b)
a = silk_per_household.numerator // silk_per_household.denominator  # Integer part
b = silk_per_household.numerator % silk_per_household.denominator  # Remainder

# Output the results
a, b
#----- content ends here -----


"""


### Explanation:
1. Convert the total silk into "銖" (the smallest unit):
   - 1 斤 = 16 两, and 1 两 = 24 銖.
   - Total silk in "銖" = (27 斤 * 16 两/斤 + 5 两) * 24 銖/两.

2. Divide the total silk in "銖" by the number of households to get the silk per household.

3. Extract the integer part (`a`) and the remainder (`b`) of the division.

### Output:
The variables `a` and `b` will contain the solution:
- `a` is the integer part of the silk each household gets in "銖".
- `b` is the remainder in "銖".
"""


"""
Variable 'a' has wrong value. Expected: 1421/100, Actual: 14
Variable 'b' has wrong value. Expected: 51/50, Actual: 26"""
