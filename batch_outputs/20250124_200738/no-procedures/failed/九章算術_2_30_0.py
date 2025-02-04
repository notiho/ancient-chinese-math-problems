"""
今有麥一斗，欲為大䵂。問︰得幾何？
荅曰：為大䵂 a斗 。
"""

#----- content starts here -----
"""
Suppose there is 1 dou of wheat. It is desired to turn it into daqu (a type of fermented grain).
Question: how much daqu does it yield?

Answer: it yields *a* dou of daqu.
"""

# 麥一斗
麥 = 1

# Conversion ratio: daqu is 4/5 of the original wheat
a = Fraction(4 * 麥, 5)

# Result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 4/5"""
