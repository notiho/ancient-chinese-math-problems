"""
今有糲飯七斗六升、七分升之四，欲為飧。問︰得幾何？
荅曰：為飧 a斗 。
"""

"""
Suppose there is 7 dou, 6 sheng, and 4/7 of a sheng of husked rice. It is desired to turn it into cooked rice (飧).
Question: how much cooked rice does it make?

Answer: it makes *a* dou of cooked rice.
"""

from fractions import Fraction

# 糲飯七斗六升、七分升之四
糲飯 = 7 + Fraction(6, 10) + Fraction(4, 70)  # Convert everything into dou (1 dou = 10 sheng)

# Cooked rice is husked rice multiplied by 2
a = 2 * 糲飯

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 1608/175, Actual: 536/35"""
