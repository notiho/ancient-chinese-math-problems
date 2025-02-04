"""
今有糲米六斗四升、五分升之三，欲為糲飯。問︰得幾何？
荅曰：為糲飯 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 6 dou, 4 sheng, and 3/5 of a sheng of roughly husked millet. It is desired to turn it into roughly husked rice (糲飯).
Question: how much roughly husked rice does it make?

Answer: it makes *a* dou of roughly husked rice.
"""

from fractions import Fraction

# 糲米六斗四升、五分升之三
糲米 = 6 + Fraction(4, 10) + Fraction(3, 50)  # Convert everything to dou (1 dou = 10 sheng)

# Conversion rate: 糲米 to 糲飯 is 4/5
a = Fraction(4, 5) * 糲米

# Result in dou
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 323/20, Actual: 646/125"""
