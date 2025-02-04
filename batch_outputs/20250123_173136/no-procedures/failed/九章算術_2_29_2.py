"""
今有麥八斗六升、七分升之三，欲為小䵂，問︰得幾何？
荅曰：為小䵂 a斗 。
"""

"""
Suppose there are 8 dou, 6 sheng, and 3/7 of a sheng of wheat. It is desired to turn it into flour.
Question: how much flour is obtained?

Answer: it makes *a* dou of flour.
"""

from fractions import Fraction

# 麥八斗六升、七分升之三
麥 = 8 + Fraction(6, 10) + Fraction(3, 70)

# Conversion rate: 1 dou of wheat produces 4/5 dou of flour
conversion_rate = Fraction(4, 5)

# Calculate the amount of flour
a = 麥 * conversion_rate

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 363/140, Actual: 242/35"""
