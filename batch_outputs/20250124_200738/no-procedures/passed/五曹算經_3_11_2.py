"""
又有席，一領坐客一十五人，有客四萬四千六百二十五人。問：席㡬何？
答曰： a領 。
"""

#----- content starts here -----
"""
Suppose there is one mat (席) that can seat 15 people. There are 44,625 guests.
Question: how many mats are needed?

Answer: *a* mats.
"""

# 一領席坐客十五人
席容量 = 15

# 客四萬四千六百二十五人
客人數 = 44625

# Calculate the number of mats needed
a = Fraction(客人數, 席容量)

# If the result is not an integer, round up since partial mats cannot exist
if a.denominator != 1:
    a = a.numerator // a.denominator + 1  # Round up to the nearest whole number#----- content ends here -----

"""
"""
