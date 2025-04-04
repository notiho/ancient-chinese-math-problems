"""
今有粟二斗，欲為櫱。問︰得幾何？
荅曰：為櫱 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 2 dou of unhusked millet. It is desired to turn it into husked millet.
Question: how much husked millet does one obtain?

Answer: it makes *a* dou of husked millet.
"""

from fractions import Fraction

# 粟二斗
粟 = 2

# Husked millet is obtained by multiplying the amount of unhusked millet by 3/5
a = Fraction(3 * 粟, 5)

# Result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 7, Actual: 6/5"""
