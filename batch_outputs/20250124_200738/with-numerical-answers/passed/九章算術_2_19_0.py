"""
今有糲米十五斗五升、五分升之二，欲為粟。問︰得幾何？
術曰：以糲米求粟，五之，三而一。
荅曰：為粟 a(=259/10)斗 。
"""

#----- content starts here -----
"""
Suppose there is 15 dou, 5 sheng, and 2/5 of a sheng of roughly husked millet. It is desired to turn it into unhusked millet.
Question: how much does one obtain?

The procedure says: when seeking unhusked millet using roughly husked millet, multiply by 5 and divide by 3.

The answer says: *a*(=259/10) dou of unhusked millet.
"""

from fractions import Fraction

# 糲米十五斗五升、五分升之二
糲米 = 15 + Fraction(5, 10) + Fraction(2, 50)  # Convert everything to dou

# 以糲米求粟，五之
粟 = 5 * 糲米

# 三而一
a = Fraction(粟, 3)  # 259/10 dou#----- content ends here -----

"""
"""
