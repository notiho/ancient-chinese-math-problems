"""
今有麥一斗，欲為大䵂。問︰得幾何？
術曰：以麥求大䵂，六之，五而一。
荅曰：為大䵂 a斗 。
"""

"""
Suppose there is one dou of wheat. It is desired to turn it into coarse flour (大䵂).
Question: how much coarse flour does one obtain?

The procedure says: when seeking coarse flour from wheat, multiply by 6 and divide by 5.

The answer says: it makes *a* dou of coarse flour.
"""

# 麥一斗
麥 = 1

# 以麥求大䵂，六之
大䵂 = 6 * 麥

# 五而一
a = Fraction(大䵂, 5)
"""
"""
