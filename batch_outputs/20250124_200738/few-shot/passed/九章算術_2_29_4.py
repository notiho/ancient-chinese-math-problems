"""
今有麥八斗六升、七分升之三，欲為小䵂，問︰得幾何？
術曰：以麥求小䵂，三之，十而一。
荅曰：為小䵂 a斗 。
"""

#----- content starts here -----
"""
Suppose there is 8 dou, 6 sheng, and 3/7 of a sheng of wheat. It is desired to turn it into xiaoqu (a processed form of wheat).
Question: how much xiaoqu does it make?

The procedure says: when seeking xiaoqu using wheat, multiply by 3 and divide by 10.

Answer: it makes *a* dou of xiaoqu.
"""

from fractions import Fraction

# 麥八斗六升、七分升之三
麥 = 8 + Fraction(6, 10) + Fraction(3, 70)

# 以麥求小䵂，三之
小䵂 = 3 * 麥

# 十而一
a = Fraction(小䵂, 10)#----- content ends here -----

"""
"""
