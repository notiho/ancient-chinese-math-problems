"""
今有麥一斗，欲為大䵂。問︰得幾何？
術曰：以麥求大䵂，六之，五而一。
荅曰：為大䵂 a(=6/5)斗 。
"""

#----- content starts here -----
"""
Suppose there is one dou of wheat. It is desired to turn it into coarse flour.
Question: how much coarse flour does one obtain?

The procedure says: when seeking coarse flour from wheat, multiply by 6 and divide by 5.

The answer says: *a*(=6/5) dou of coarse flour.
"""

# 麥一斗
麥 = 1

# 以麥求大䵂，六之
大䵂 = 6 * 麥

# 五而一
a = Fraction(大䵂, 5) # 6/5 dou#----- content ends here -----

"""
"""
