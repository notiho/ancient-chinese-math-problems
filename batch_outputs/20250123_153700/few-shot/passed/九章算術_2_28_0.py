"""
今有菽二斗，欲為豉。問︰得幾何？
術曰：以菽求豉，七之，五而一。
荅曰：為豉 a斗 。
"""

"""
Suppose there are 2 dou of beans. It is desired to turn them into fermented beans (chi).
Question: how much fermented beans does one obtain?

The procedure says: when seeking fermented beans from beans, multiply by 7 and divide by 5.

The answer says: it makes *a* dou of fermented beans.
"""

# 菽二斗
菽 = 2

# 以菽求豉，七之
豉 = 7 * 菽

# 五而一
a = Fraction(豉, 5)
"""
"""
