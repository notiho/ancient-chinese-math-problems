"""
今有粟七斗五升、七分升之四，欲為稻。問︰得幾何？
荅曰：為稻 a斗 。
"""

#----- content starts here -----
"""
Suppose there is 7 dou, 5 sheng, and 4/7 of a sheng of millet. It is desired to turn it into rice.
Question: how much rice does one obtain?

Answer: it makes *a* dou of rice.
"""

from fractions import Fraction

# 粟七斗五升、七分升之四
粟 = 7 + Fraction(5, 10) + Fraction(4, 70)

# Conversion ratio: millet to rice is 2/3
a = Fraction(2, 3) * 粟

# Result in dou
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1587/175, Actual: 529/105"""
