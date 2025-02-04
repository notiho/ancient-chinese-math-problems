"""
今有麥八斗六升、七分升之三，欲為小䵂，問︰得幾何？
術曰：以麥求小䵂，三之，十而一。
荅曰：為小䵂 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 8 dou, 6 sheng, and 3/7 of a sheng of wheat. It is desired to turn it into small flour.
Question: how much small flour is obtained?

The procedure says: When seeking small flour using wheat, multiply by 3 and divide by 10.

Answer: it makes *a* dou of small flour.
"""

from fractions import Fraction

# 麥八斗六升、七分升之三
麥 = 8  # 8 dou
麥 += Fraction(6, 10)  # 6 sheng (1 dou = 10 sheng)
麥 += Fraction(3, 7 * 10)  # 3/7 of a sheng (convert to dou)

# 以麥求小䵂，三之
小䵂 = 3 * 麥

# 十而一
a = Fraction(小䵂, 10)

# Output the result
a#----- content ends here -----

"""
"""
