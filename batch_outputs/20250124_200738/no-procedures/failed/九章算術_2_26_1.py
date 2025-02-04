"""
今有糲飯七斗六升、七分升之四，欲為飧。問︰得幾何？
荅曰：為飧 a斗 。
"""

#----- content starts here -----
"""
Suppose there is 7 dou, 6 sheng, and 4/7 of a sheng of coarse rice. It is desired to turn it into cooked rice (飧).
Question: how much cooked rice does it make?

Answer: it makes *a* dou of cooked rice.
"""

from fractions import Fraction

# 糲飯 7斗6升4/7升
糲飯 = 7 * 10 + 6 + Fraction(4, 7)  # Convert everything to sheng (1 dou = 10 sheng)

# Cooked rice is 2.5 times the volume of coarse rice
飧 = 糲飯 * Fraction(5, 2)

# Convert back to dou
a = 飧 / 10  # 1 dou = 10 sheng

# Output
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1608/175, Actual: 134/7"""
