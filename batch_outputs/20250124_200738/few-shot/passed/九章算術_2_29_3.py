"""
今有麥八斗六升、七分升之三，欲為小䵂，問︰得幾何？
術曰：以麥求小䵂，三之，十而一。
荅曰：為小䵂 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 8 dou, 6 sheng, and 3/7 of a sheng of wheat. It is desired to turn it into flour.
Question: how much flour is obtained?

The procedure says: When seeking flour from wheat, multiply by 3 and divide by 10.

Answer: it makes *a* dou of flour.
"""

from fractions import Fraction

# 麥八斗六升、七分升之三
麥 = 8  # 8斗
麥 += Fraction(6, 10)  # 6升 (1斗 = 10升)
麥 += Fraction(3, 70)  # 3/7升 (1升 = 1/10斗, so 1/7升 = 1/70斗)

# 以麥求小䵂，三之
小䵂 = 3 * 麥

# 十而一
a = Fraction(小䵂, 10)  # 答案以斗為單位#----- content ends here -----

"""
"""
