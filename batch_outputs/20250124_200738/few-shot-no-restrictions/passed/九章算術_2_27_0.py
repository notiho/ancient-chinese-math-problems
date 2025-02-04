"""
今有菽一斗，欲為熟菽。問︰得幾何？
術曰：以菽求熟菽，二十三之，十而一。
荅曰：為熟菽 a斗 。
"""

#----- content starts here -----
"""
Suppose there is 1 dou of beans (菽). It is desired to turn it into cooked beans (熟菽).
Question: how much cooked beans does one obtain?

The procedure says: When seeking cooked beans using raw beans, multiply by 23 and divide by 10.

Answer: it makes *a* dou of cooked beans.
"""

from fractions import Fraction

# 菽一斗
菽 = 1

# 以菽求熟菽，二十三之
熟菽 = 23 * 菽

# 十而一
a = Fraction(熟菽, 10)

# Output the result
a#----- content ends here -----

"""
"""
