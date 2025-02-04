"""
今有圭田從三十步一頭廣二十四步一頭無步。問：為田㡬何？
術曰：列一頭廣二十四步半之得一十二步以從三十步乘之得三百六十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a wedge-shaped field. One side of the length is 30 bu, one side of the width is 24 bu, and the other side of the width is 0 bu.
Question: how large is the field?

The procedure says: Take one side of the width (24 bu), halve it to get 12 bu. Multiply this by the length (30 bu) to get the total area in bu². Divide this by the mu-divisor (240 bu² per mu) to get the area in mu.

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# Given dimensions
從 = 30  # Length in bu
廣 = 24  # Width at one end in bu
無 = 0   # Width at the other end in bu

# Halve the width (廣)
平均廣 = Fraction(廣 + 無, 2)

# Multiply by the length (從) to get the total area in bu²
積步 = 平均廣 * 從

# Divide by the mu-divisor (240 bu² per mu) to get the area in mu
畝法 = 240
畝數 = Fraction(積步, 畝法)

# Separate the result into whole mu and remaining bu
a = 畝數.numerator // 畝數.denominator  # Whole mu
b = 畝數.numerator % 畝數.denominator  # Remaining bu

# Output
a, b#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 120, Actual: 1"""
