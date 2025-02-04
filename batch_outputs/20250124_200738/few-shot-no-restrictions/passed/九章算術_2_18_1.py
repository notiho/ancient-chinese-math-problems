"""
今有粟二斗，欲為櫱。問︰得幾何？
術曰：以粟求櫱，七之，二而一。
荅曰：為櫱 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 2 dou of millet. It is desired to turn it into niè (sprouted grain).
Question: how much sprouted grain is obtained?

The procedure says: When seeking niè (sprouted grain) from millet, multiply by 7 and divide by 2.

Answer: it makes *a* dou of niè.
"""

from fractions import Fraction

# 粟二斗
粟 = 2

# 以粟求櫱，七之
櫱 = 7 * 粟

# 二而一
a = Fraction(櫱, 2)

# Answer
a  # Result in dou#----- content ends here -----

"""
"""
