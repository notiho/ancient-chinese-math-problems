"""
今有圭田從三十步一頭廣二十四步一頭無步。問：為田㡬何？
術曰：列一頭廣二十四步半之得一十二步以從三十步乘之得三百六十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a wedge-shaped field (圭田) with one side of length 30 bu, one side of width 24 bu, and the other side of width 0 bu.
Question: how large is the field?

The procedure says: Take the width of one side (24 bu), halve it to get 12 bu.
Multiply this by the length (30 bu) to get the total area in bu².
Divide the total area by the mu-divisor (240 bu² per mu) to get the area in mu.

Answer: *a* mu and *b* bu².
"""

from fractions import Fraction

# Given dimensions
從 = 30  # Length in bu
廣 = 24  # Width in bu
無 = 0   # Other width in bu

# Halve the width
半廣 = 廣 / 2

# Calculate the area in bu²
積步 = 半廣 * 從

# Divide by the mu-divisor (240 bu² per mu)
畝法 = 240
畝數 = Fraction(積步, 畝法)

# Separate into integer mu and remaining bu²
a = 畝數.numerator // 畝數.denominator  # Integer part (mu)
b = 畝數.numerator % 畝數.denominator   # Remaining bu²

# Output
a, b#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
