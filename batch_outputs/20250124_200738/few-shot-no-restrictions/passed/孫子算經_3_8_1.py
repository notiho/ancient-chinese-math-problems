"""
今有綿，九萬一千一百三十五觔，給與三萬六千四百五十四戶。問：戶得幾何？
術曰：置九萬一千一百三十五觔，為實；以三萬六千四百五十四戶，為法。除之，得二觔，不盡一萬八千二百二十七觔，以一十六乘之，得二十九萬一千六百三十二兩，以戶除之，即得。
答曰： a觔 。
"""

#----- content starts here -----
"""
Suppose there are 91,135 jin of cotton, to be distributed among 36,454 households.
Question: how much does each household receive?

The procedure says: Place 91,135 jin as the dividend (實), and 36,454 households as the divisor (法). 
Divide them, obtaining 2 jin, with a remainder of 18,227 jin.
Multiply the remainder by 16, obtaining 291,632 liang.
Divide this by the number of households, obtaining the fractional part.

Answer: *a* jin.
"""

from fractions import Fraction

# Total cotton in jin
綿 = 91135

# Total households
戶 = 36454

# First division: Divide jin by households
商 = 綿 // 戶  # Quotient in jin
餘 = 綿 % 戶   # Remainder in jin

# Convert remainder jin to liang (1 jin = 16 liang)
餘量 = 餘 * 16

# Divide liang by households to get fractional part
分量 = Fraction(餘量, 戶)

# Final result: total jin per household
a = 商 + 分量 / 16  # Convert fractional liang back to jin

a#----- content ends here -----

"""
"""
