"""
今有糲米十五斗五升、五分升之二，欲為粟。問︰得幾何？
荅曰：為粟 a斗 。
"""

"""
Suppose there are 15 dou, 5 sheng, and 2/5 of a sheng of roughly husked millet. It is desired to turn it back into unhusked millet.
Question: how much unhusked millet does it make?

Answer: it makes *a* dou of unhusked millet.
"""

from fractions import Fraction

# 糲米十五斗五升、五分升之二
糲米 = 15 + Fraction(5, 10) + Fraction(2, 50)  # Convert everything to dou (1 dou = 10 sheng)

# To convert husked millet back to unhusked millet, multiply by 5/3
a = 糲米 * Fraction(5, 3)

# Result
a
"""
"""
