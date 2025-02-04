"""
今有粟一斗，欲為小䵂。問︰得幾何？
荅曰：為小䵂 a升 。
"""

#----- content starts here -----
"""
Suppose there is one dou of millet. It is desired to turn it into finely husked rice (小䵂).
Question: how much finely husked rice is obtained?

Answer: it makes *a* sheng of finely husked rice.
"""

from fractions import Fraction

# 粟一斗
粟 = 1  # in dou

# Convert dou to sheng (1 dou = 10 sheng)
粟_in_sheng = 10 * 粟

# Finely husked rice is obtained by multiplying by 2/5
a = Fraction(2 * 粟_in_sheng, 5)

# Result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 27/10, Actual: 4"""
