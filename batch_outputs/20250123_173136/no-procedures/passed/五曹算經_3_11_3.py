"""
又有席，一領坐客一十五人，有客四萬四千六百二十五人。問：席㡬何？
答曰： a領 。
"""

"""
Suppose there is one mat (席) that can seat 15 people. There are 44,625 guests.
Question: how many mats are required?

Answer: *a* mats.
"""

# 一領席坐客 15 人
席容量 = 15

# 客人數 44,625 人
客人數 = 44625

# Calculate the number of mats required
# Divide the total number of guests by the capacity of one mat
a = Fraction(客人數, 席容量)

# Since we cannot have a fraction of a mat, we round up to the nearest whole number
# If there is any remainder, we need one additional mat
if 客人數 % 席容量 != 0:
    a = a.numerator // a.denominator + 1
else:
    a = a.numerator // a.denominator

a  # Output the number of mats required
"""
"""
