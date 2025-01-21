"""
今有麥一斗欲為大䵂問得幾何
術曰以麥求大䵂六之五而一
荅曰為大䵂 a斗 
"""

"""
Suppose there is one dou of wheat. It is desired to turn it into daqu (a type of fermented grain).
Question: how much daqu is obtained?

The procedure says: When seeking daqu from wheat, multiply by 6 and divide by 5.

The answer says: it makes *a* dou of daqu.
"""

# 麥一斗
麥 = 1

# 以麥求大䵂，六之
大䵂 = 6 * 麥

# 五而一
a = Fraction(大䵂, 5)
"""
"""
