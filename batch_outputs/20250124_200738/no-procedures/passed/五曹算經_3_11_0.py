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

# One mat can seat 15 people
mat_capacity = 15

# Total number of guests
guests = 44625

# Calculate the number of mats needed
a = Fraction(guests, mat_capacity)  # Use Fraction to represent the exact number of mats needed#----- content ends here -----

"""
"""
