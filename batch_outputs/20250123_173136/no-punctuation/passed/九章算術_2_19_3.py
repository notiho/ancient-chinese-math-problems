"""
今有糲米十五斗五升五分升之二欲為粟問得幾何
術曰以糲米求粟五之三而一
荅曰為粟 a斗 
"""

"""
Suppose there are 15 dou, 5 sheng, and 2/5 of a sheng of roughly husked millet.
It is desired to turn it into unhusked millet.
Question: how much does one obtain?

The procedure says: when seeking unhusked millet from roughly husked millet, multiply by 5 and divide by 3.

The answer says: it makes *a* dou of unhusked millet.
"""

from fractions import Fraction

# 糲米十五斗五升五分升之二
糲米 = 15 * 10 + 5 + Fraction(2, 5)  # Convert everything to sheng (1 dou = 10 sheng)

# 以糲米求粟，五之
粟 = 5 * 糲米

# 三而一
粟 = Fraction(粟, 3)

# Convert back to dou
a = Fraction(粟, 10)  # Convert sheng to dou (1 dou = 10 sheng)
"""
"""
