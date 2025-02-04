"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a銖 奇 b銖 。
"""

"""
To solve this problem, we need to calculate how much silk (in "銖") each household gets. Here's the Python code to compute the values of the unknowns `a` and `b`:


"""


from fractions import Fraction

# Given data
total_silk_jin = 27  # Total silk in jin
total_silk_liang = 5  # Additional silk in liang
total_households = 738  # Total households

# Convert silk to 銖
silk_liang = total_silk_jin * 16 + total_silk_liang  # Convert jin to liang and add the extra liang
silk_zhu = silk_liang * 24  # Convert liang to zhu

# Divide silk among households
silk_per_household = Fraction(silk_zhu, total_households)

# Extract the integer part (a) and the remainder (b)
a = silk_per_household.numerator // silk_per_household.denominator  # Integer part
b = silk_per_household.numerator % silk_per_household.denominator  # Remainder

# Results
a = Fraction(a)  # Ensure a is a Fraction
b = Fraction(b, silk_per_household.denominator)  # Remainder as a Fraction


"""


The variables `a` and `b` now contain the solution to the problem.
"""


"""
Variable 'a' has wrong value. Expected: 1421/100, Actual: 14
Variable 'b' has wrong value. Expected: 51/50, Actual: 26/123"""
