"""
今有糲飯七斗六升、七分升之四，欲為飧。問︰得幾何？
荅曰：為飧 a斗 。
"""

"""
Suppose there is 7 dou, 6 sheng, and 4/7 of a sheng of roughly husked rice. It is desired to turn it into cooked rice (suan).
Question: how much cooked rice does it make?

Answer: it makes *a* dou of cooked rice.
"""

from fractions import Fraction

# 糲飯 7斗6升7分升之4
糲飯 = 7 + Fraction(6, 10) + Fraction(4, 70)

# Cooked rice is 2 times the volume of roughly husked rice
a = 2 * 糲飯

# Result
a
"""
Variable 'a' has wrong value. Expected: 1608/175, Actual: 536/35"""
