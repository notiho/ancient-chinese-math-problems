"""
今有粟二斗，欲為櫱。問︰得幾何？
荅曰：為櫱 a斗 。
"""

"""
Suppose there are 2 dou of millet. It is desired to turn it into sprouts (櫱).
Question: how much sprouts does one obtain?

Answer: it makes *a* dou of sprouts.
"""

from fractions import Fraction

# 粟二斗
粟 = 2

# Sprouts are obtained by multiplying the millet by 7/10
a = Fraction(7 * 粟, 10)

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 7, Actual: 7/5"""
