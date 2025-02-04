"""
今有粟二斗欲為櫱問得幾何
術曰以粟求櫱七之二而一
荅曰為櫱 a斗 
"""

"""
Suppose there are 2 dou of millet. It is desired to turn it into bran (櫱).
Question: how much bran does one obtain?

The procedure says: when seeking bran from millet, multiply by 7 and divide by 2.

The answer says: it makes *a* dou of bran.
"""

# 粟二斗
粟 = 2

# 以粟求櫱，七之
櫱 = 7 * 粟

# 二而一
a = Fraction(櫱, 2)
"""
"""
