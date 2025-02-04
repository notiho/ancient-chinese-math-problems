"""
今有糲米六斗四升、五分升之三，欲為糲飯。問︰得幾何？
術曰：以糲米求糲飯，五之，二而一。
荅曰：為糲飯 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 6 dou, 4 sheng, and 3/5 of a sheng of roughly husked millet. It is desired to turn it into roughly husked rice.
Question: how much roughly husked rice does it make?

The procedure says: When seeking roughly husked rice from roughly husked millet, multiply by 5 and divide by 2.

The answer says: it makes *a* dou of roughly husked rice.
"""

from fractions import Fraction

# 糲米六斗四升、五分升之三
糲米 = 6 * 10 + 4 + Fraction(3, 5)  # Convert to sheng (1 dou = 10 sheng)

# 以糲米求糲飯，五之
糲飯 = 5 * 糲米

# 二而一
糲飯 = Fraction(糲飯, 2)

# Convert back to dou and sheng
a斗 = 糲飯 // 10  # Whole dou
a升 = 糲飯 % 10   # Remaining sheng

a = f"{a斗}斗 {a升}升"  # Final result in dou and sheng#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 323/20, Actual: 16斗 3/2升"""
