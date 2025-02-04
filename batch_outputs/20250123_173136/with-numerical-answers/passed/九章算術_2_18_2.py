"""
今有粟二斗，欲為櫱。問︰得幾何？
術曰：以粟求櫱，七之，二而一。
荅曰：為櫱 a(=7)斗 。
"""

"""
Suppose there are 2 dou of millet. It is desired to turn it into niè (sprouted grain).
Question: how much does one obtain?

The procedure says: when seeking niè from millet, multiply by 7 and divide by 2.

The answer says: *a*(=7) dou of niè.
"""

# 粟二斗
粟 = 2

# 以粟求櫱，七之
櫱 = 7 * 粟

# 二而一
a = Fraction(櫱, 2) # 7 dou
"""
"""
