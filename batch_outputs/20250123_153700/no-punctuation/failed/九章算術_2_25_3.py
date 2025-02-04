"""
今有糲米六斗四升五分升之三欲為糲飯問得幾何
術曰以糲米求糲飯五之二而一
荅曰為糲飯 a斗 
"""

"""
Suppose there are 6 dou, 4 sheng, and 3/5 of a sheng of roughly husked millet.
It is desired to turn it into roughly husked millet rice.
Question: how much does one obtain?

The procedure says: when seeking roughly husked millet rice from roughly husked millet, multiply by 5 and divide by 2.

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
a_斗 = 糲飯 // 10  # Whole dou
a_升 = 糲飯 % 10   # Remaining sheng

a = f"{a_斗}斗 {a_升}升"

"""
Variable 'a' has wrong value. Expected: 323/20, Actual: 16斗 3/2升"""
