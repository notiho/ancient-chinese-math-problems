"""
今有糲米十五斗五升五分升之二欲為粟問得幾何
術曰以糲米求粟五之三而一
荅曰為粟 a斗 
"""

#----- content starts here -----
"""
Suppose there are 15 dou, 5 sheng, and 2/5 of a sheng of roughly husked millet.
It is desired to turn it back into unhusked millet.
Question: how much unhusked millet does it make?

The procedure says: when seeking unhusked millet using roughly husked millet, multiply by 5 and divide by 3.

The answer says: it makes *a* dou of unhusked millet.
"""

from fractions import Fraction

# 糲米十五斗五升五分升之二
糲米 = 15 + Fraction(5, 10) + Fraction(2, 50)  # Convert everything to dou

# 以糲米求粟，五之
粟 = 5 * 糲米

# 三而一
a = Fraction(粟, 3)  # Result in dou#----- content ends here -----

"""
"""
