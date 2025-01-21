"""
今有糲米十五斗五升五分升之二欲為粟問得幾何
術曰以糲米求粟五之三而一
荅曰為粟 a斗 
"""

"""
Suppose there are 15 dou, 5 sheng, and 2/5 of a sheng of roughly husked millet. 
It is desired to turn it back into unhusked millet.
Question: how much unhusked millet does it make?

The procedure says: when seeking unhusked millet using roughly husked millet, multiply by 5 and divide by 3.

The answer says: it makes *a* dou of unhusked millet.
"""

from fractions import Fraction

# 糲米十五斗五升五分升之二
糲米 = 15 * 10 + 5 + Fraction(2, 5)  # Convert to sheng (1 dou = 10 sheng)

# 以糲米求粟，五之
粟 = 5 * 糲米

# 三而一
粟 = Fraction(粟, 3)

# Convert back to dou and sheng
粟斗 = int(粟 // 10)  # Whole dou
粟升 = 粟 % 10        # Remaining sheng

a = Fraction(粟斗 * 10 + 粟升, 10)  # Final result in dou
"""
"""
