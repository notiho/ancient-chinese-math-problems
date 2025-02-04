"""
又有席，一領坐客一十五人，有客四萬四千六百二十五人。問：席㡬何？
術曰：列四萬四千六百二十五人，以一十五人除之即得。
答曰： a領 。
"""

#----- content starts here -----
"""
Suppose there is one mat (席), which can seat 15 people. 
There are 44,625 guests. 
Question: how many mats are required?

The procedure says: Place 44,625 guests, divide by 15 people per mat, and the result is the number of mats.

Answer: *a* mats.
"""

# 客四萬四千六百二十五人
客人數 = 44625

# 一領坐客一十五人
每席人數 = 15

# 以一十五人除之即得
a = Fraction(客人數, 每席人數)  # Use Fraction to represent exact result if not an integer

# Output the result
a#----- content ends here -----

"""
"""
