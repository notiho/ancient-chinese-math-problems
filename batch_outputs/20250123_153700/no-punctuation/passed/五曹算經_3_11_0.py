"""
又有席一領坐客一十五人有客四萬四千六百二十五人問席㡬何？
術曰列四萬四千六百二十五人以一十五人除之即得
答曰 a領 
"""

"""
Suppose there is one mat that accommodates 15 people. 
There are 44,625 people in total.
Question: how many mats are needed?

The procedure says: Arrange the 44,625 people and divide by 15 people. 
The result is the number of mats.

Answer: *a* mats.
"""

# 客四萬四千六百二十五人
客人數 = 44625

# 坐客一十五人
每席人數 = 15

# 以一十五人除之，即得
a = Fraction(客人數, 每席人數)
"""
"""
