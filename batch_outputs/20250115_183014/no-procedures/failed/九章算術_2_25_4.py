"""
今有糲米六斗四升、五分升之三，欲為糲飯。問︰得幾何？
荅曰：為糲飯 a斗 。
"""

"""
Suppose there is 6 dou, 4 sheng, and 3/5 of a sheng of roughly husked millet. It is desired to turn it into roughly cooked millet rice.
Question: how much cooked millet rice does it make?

Answer: it makes *a* dou of cooked millet rice.
"""

from fractions import Fraction

# 糲米六斗四升、五分升之三
糲米 = 6 + Fraction(4, 10) + Fraction(3, 50)  # Convert everything into dou (1 dou = 10 sheng)

# Conversion ratio: cooked millet rice is 4/3 times the husked millet
a = Fraction(4, 3) * 糲米  # Result in dou

a
"""
Variable 'a' has wrong value. Expected: 323/20, Actual: 646/75"""
