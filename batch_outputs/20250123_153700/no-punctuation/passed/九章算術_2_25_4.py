"""
今有糲米六斗四升五分升之三欲為糲飯問得幾何
術曰以糲米求糲飯五之二而一
荅曰為糲飯 a斗 
"""

"""
Suppose there is 6 dou, 4 sheng, and 3/5 of a sheng of roughly husked millet.
It is desired to turn it into roughly husked millet rice.
Question: how much does one obtain?

The procedure says: when seeking roughly husked millet rice using roughly husked millet, multiply by 5 and divide by 2.

The answer says: it makes *a* dou of roughly husked millet rice.
"""

from fractions import Fraction

# 糲米六斗四升五分升之三
糲米 = 6 * 10 + 4 + Fraction(3, 5)  # Convert to sheng (1 dou = 10 sheng)

# 以糲米求糲飯，五之
糲飯 = 5 * 糲米

# 二而一
糲飯 = Fraction(糲飯, 2)

# Convert back to dou and sheng
a斗 = 糲飯 // 10  # Whole dou
a升 = 糲飯 % 10   # Remaining sheng

a = Fraction(a斗) + Fraction(a升, 10)  # Final result in dou
"""
"""
