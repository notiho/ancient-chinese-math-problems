"""
今有綿，九萬一千一百三十五觔，給與三萬六千四百五十四戶。問：戶得幾何？
術曰：置九萬一千一百三十五觔，為實；以三萬六千四百五十四戶，為法。除之，得二觔，不盡一萬八千二百二十七觔，以一十六乘之，得二十九萬一千六百三十二兩，以戶除之，即得。
答曰： a觔 。
"""

#----- content starts here -----
"""
Suppose there are 91,135 jin of cotton, to be distributed among 36,454 households.
Question: how much does each household receive?

The procedure says: Place 91,135 jin as the dividend, and 36,454 households as the divisor.
Divide them, obtaining 2 jin, with a remainder of 18,227 jin.
Multiply the remainder by 16, obtaining 291,632 liang.
Divide this by the number of households, and the result is the fractional part.

Answer: each household gets *a* jin.
"""

from fractions import Fraction

# Total cotton in jin
綿 = 91135

# Total households
戶 = 36454

# First division: whole jin per household
whole_jin_per_household = 綿 // 戶

# Remainder in jin
remainder_jin = 綿 % 戶

# Convert remainder jin to liang (1 jin = 16 liang)
remainder_liang = remainder_jin * 16

# Distribute liang among households
liang_per_household = Fraction(remainder_liang, 戶)

# Total jin per household (including fractional part)
a = whole_jin_per_household + Fraction(liang_per_household, 16)

# Output the result
a#----- content ends here -----

"""
"""
