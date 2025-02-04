"""
今有麥一斗，欲為大䵂。問︰得幾何？
術曰：以麥求大䵂，六之，五而一。
荅曰：為大䵂 a斗 。
"""

#----- content starts here -----
"""
Suppose there is 1 dou of wheat. It is desired to turn it into daqu (a type of fermented grain product).
Question: how much daqu is obtained?

The procedure says: When seeking daqu from wheat, multiply by 6 and divide by 5.

Answer: it makes *a* dou of daqu.
"""

from fractions import Fraction

# 麥一斗
麥 = 1

# 以麥求大䵂，六之
大䵂 = 6 * 麥

# 五而一
a = Fraction(大䵂, 5)

# Output the result
a#----- content ends here -----

"""
"""
