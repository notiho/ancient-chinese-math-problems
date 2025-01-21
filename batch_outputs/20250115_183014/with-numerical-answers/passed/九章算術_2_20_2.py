"""
今有粺米二斗，欲為粟。問︰得幾何？
術曰：以粺米求粟，五十之，二十七而一。
荅曰：為粟 a(=100/27)斗 。
"""

"""
Suppose there are 2 dou of polished rice. It is desired to turn it into unhusked millet.
Question: how much does one obtain?

The procedure says: when seeking unhusked millet using polished rice, multiply by 50 and divide by 27.

The answer says: *a*(=100/27) dou of unhusked millet.
"""

# 粺米二斗
粺米 = 2

# 以粺米求粟，五十之
粟 = 50 * 粺米

# 二十七而一
a = Fraction(粟, 27) # 100/27

"""
"""
