"""
今有麥八斗六升、七分升之三，欲為小䵂，問︰得幾何？
術曰：以麥求小䵂，三之，十而一。
荅曰：為小䵂 a斗 。
"""

"""

"""


from fractions import Fraction

# 麥八斗六升、七分升之三
麥 = 8  # 斗
麥 += 6 / 10  # 6升轉為斗
麥 += Fraction(3, 7 * 10)  # 7分升之3轉為斗

# 以麥求小䵂，三之
小䵂 = 3 * 麥

# 十而一
a = Fraction(小䵂, 10)


"""

"""


"""
Code error: both arguments should be Rational instances"""
