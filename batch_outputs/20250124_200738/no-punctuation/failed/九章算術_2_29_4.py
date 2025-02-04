"""
今有麥八斗六升七分升之三欲為小䵂問得幾何
術曰以麥求小䵂三之十而一
荅曰為小䵂 a斗 
"""

#----- content starts here -----
"""
Suppose there is 8 dou, 6 sheng, and 7/10 of a sheng of wheat. It is desired to turn it into xiaoqu (a processed form of wheat).
Question: how much xiaoqu does one obtain?

The procedure says: when seeking xiaoqu from wheat, multiply by 3 and divide by 10.

The answer says: it makes *a* dou of xiaoqu.
"""

# 麥八斗六升七分升之三
麥斗 = 8
麥升 = 6
麥分升 = Fraction(7, 10)

# Convert everything to sheng (1 dou = 10 sheng)
總升 = (麥斗 * 10) + 麥升 + 麥分升

# 以麥求小䵂，三之
小䵂 = 3 * 總升

# 十而一
小䵂斗 = Fraction(小䵂, 10)

a = 小䵂斗#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 363/140, Actual: 2601/100"""
