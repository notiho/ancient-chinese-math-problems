"""
今有麥一斗，欲為大䵂。問︰得幾何？
荅曰：為大䵂 a斗 。
"""

"""
Suppose there is 1 dou of wheat. It is desired to turn it into daqu (a type of fermented grain).
Question: how much daqu is obtained?

Answer: it makes *a* dou of daqu.
"""

# 麥一斗
麥 = 1

# Conversion ratio: 4/5 of the original wheat becomes daqu
a = Fraction(4, 5) * 麥

# Result
a
"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 4/5"""
