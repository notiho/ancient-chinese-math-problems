"""
今有糲米十五斗五升、五分升之二，欲為粟。問︰得幾何？
術曰：以糲米求粟，五之，三而一。
荅曰：為粟 a斗 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 糲米十五斗五升、五分升之二
糲米 = 15 + Fraction(5, 10) + Fraction(2, 50)  # 15斗5升2/5升

# 以糲米求粟，五之
粟 = 5 * 糲米

# 三而一
a = Fraction(粟, 3)  # 粟的數量
#----- content ends here -----


"""

"""


"""
"""
