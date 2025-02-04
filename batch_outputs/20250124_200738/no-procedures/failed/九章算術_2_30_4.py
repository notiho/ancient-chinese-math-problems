"""
今有麥一斗，欲為大䵂。問︰得幾何？
荅曰：為大䵂 a斗 。
"""

#----- content starts here -----
"""
Suppose there is 1 dou of wheat. It is desired to turn it into daqu (a type of fermented grain).
Question: how much daqu does it produce?

Answer: it produces *a* dou of daqu.
"""

# 麥一斗
麥 = 1

# To produce daqu, multiply by 2 and divide by 3
a = Fraction(2 * 麥, 3)

# Result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 2/3"""
