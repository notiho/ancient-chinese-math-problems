"""
今有糲飯七斗六升、七分升之四，欲為飧。問︰得幾何？
術曰：以糲飯求飧，六之，五而一。
荅曰：為飧 a斗 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 糲飯七斗六升、七分升之四
糲飯 = 7 + Fraction(6, 10) + Fraction(4, 70)

# 以糲飯求飧，六之
飧 = 6 * 糲飯

# 五而一
a = Fraction(飧, 5)
#----- content ends here -----


"""

"""


"""
"""
