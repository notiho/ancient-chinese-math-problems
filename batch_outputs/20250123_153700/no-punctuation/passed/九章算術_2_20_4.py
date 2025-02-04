"""
今有粺米二斗欲為粟問得幾何
術曰以粺米求粟五十之二十七而一
荅曰為粟 a斗 
"""

"""
Suppose there are 2 dou of polished rice. It is desired to turn it into unhusked millet.
Question: how much does one obtain?

The procedure says: when seeking unhusked millet from polished rice, multiply by 50 and divide by 27.

The answer says: it makes *a* dou of unhusked millet.
"""

# 粺米二斗
粺米 = 2

# 以粺米求粟，五十之
粟 = 50 * 粺米

# 二十七而一
a = Fraction(粟, 27)
"""
"""
