"""
今有四不等田東三十五步西四十五步南二十五步北一十五步。問：為田㡬何？
術曰：并東西得八十步半之得四十步又并南北得四十步半之得二十步二位相乘得八百步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is an irregular quadrilateral field with the following dimensions:
East side: 35 bu, West side: 45 bu, South side: 25 bu, North side: 15 bu.
Question: how large is the area of the field?

The procedure says: Add the east and west sides, obtaining 80 bu, and take half of it, obtaining 40 bu.
Then add the south and north sides, obtaining 40 bu, and take half of it, obtaining 20 bu.
Multiply these two results, obtaining 800 bu².
Divide by the mu divisor (240 bu² per mu) to obtain the area.

Answer: *a* mu and *b* bu².
"""

from fractions import Fraction

# Dimensions of the field
東 = 35  # East side in bu
西 = 45  # West side in bu
南 = 25  # South side in bu
北 = 15  # North side in bu

# 畝法 (240 bu² per mu)
畝法 = 240

# Add east and west, then take half
東西平均 = (東 + 西) / 2

# Add south and north, then take half
南北平均 = (南 + 北) / 2

# Multiply the two averages to get the total area in bu²
總積步 = 東西平均 * 南北平均

# Divide by 畝法 to get the area in mu
畝數 = Fraction(總積步, 畝法)

# Extract the integer part (mu) and the remainder (bu²)
a = 畝數.numerator // 畝數.denominator  # Integer part (mu)
b = 畝數.numerator % 畝數.denominator  # Remainder (bu²)

# Final result
a_mu = a
b_bu = b
#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
