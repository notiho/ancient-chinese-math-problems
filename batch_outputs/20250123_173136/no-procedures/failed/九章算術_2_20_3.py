"""
今有粺米二斗，欲為粟。問︰得幾何？
荅曰：為粟 a斗 。
"""

"""
Suppose there are 2 dou of polished rice (粺米). It is desired to turn it back into unhusked millet (粟).
Question: how much unhusked millet does it make?

Answer: it makes *a* dou of unhusked millet.
"""

from fractions import Fraction

# 粺米二斗
粺米 = 2

# To convert polished rice back to unhusked millet, multiply by 5/3
a = Fraction(5 * 粺米, 3)

# Result
a
"""
Variable 'a' has wrong value. Expected: 100/27, Actual: 10/3"""
