"""
又有席一領坐客一十五人有客四萬四千六百二十五人問席㡬何？
術曰列四萬四千六百二十五人以一十五人除之即得
答曰 a領 
"""

#----- content starts here -----
"""
Suppose there is one mat (席) that can seat 15 people. There are 44,625 people.
Question: how many mats are required?

The procedure says: Arrange 44,625 people and divide by 15 people. The result is obtained.

Answer: *a* mats.
"""

# 客四萬四千六百二十五人
客人數 = 44625

# 坐客一十五人
每席人數 = 15

# 以一十五人除之，即得
a = Fraction(客人數, 每席人數)#----- content ends here -----

"""
"""
