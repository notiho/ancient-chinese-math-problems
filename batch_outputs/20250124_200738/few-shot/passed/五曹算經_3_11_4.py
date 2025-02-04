"""
又有席，一領坐客一十五人，有客四萬四千六百二十五人。問：席㡬何？
術曰：列四萬四千六百二十五人，以一十五人除之即得。
答曰： a領 。
"""

#----- content starts here -----
"""
Suppose there is one mat that accommodates 15 guests. There are 44,625 guests.
Question: how many mats are needed?

The procedure says: Place the 44,625 guests, and divide by 15 guests per mat to obtain the result.

Answer: *a* mats.
"""

# 客四萬四千六百二十五人
客人數 = 44625

# 一領坐客一十五人
每席客人數 = 15

# 以一十五人除之即得
a = Fraction(客人數, 每席客人數)#----- content ends here -----

"""
"""
