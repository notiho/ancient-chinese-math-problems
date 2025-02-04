"""
今有菽二斗，欲為豉。問︰得幾何？
術曰：以菽求豉，七之，五而一。
荅曰：為豉 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 2 dou of beans (菽). It is desired to turn them into fermented soybeans (豉).
Question: how much fermented soybeans does it make?

The procedure says: when seeking fermented soybeans using beans, multiply by 7 and divide by 5.

The answer says: it makes *a* dou of fermented soybeans.
"""

from fractions import Fraction

# 菽二斗
菽 = 2

# 以菽求豉，七之
豉 = 7 * 菽

# 五而一
a = Fraction(豉, 5)

# Output the result
a#----- content ends here -----

"""
"""
