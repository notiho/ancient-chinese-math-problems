"""
今有粟四斗，欲為熟菽。問︰得幾何？
術曰：以粟求熟菽，二百七之，百而一。
荅曰：為熟菽 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 4 dou of millet, and it is desired to turn it into cooked beans.
Question: how much cooked beans does it make?

The procedure says: When seeking cooked beans using millet, multiply by 207 and divide by 100.

Answer: it makes *a* dou of cooked beans.
"""

from fractions import Fraction

# 粟四斗
粟 = 4

# 以粟求熟菽，二百七之
熟菽 = 207 * 粟

# 百而一
a = Fraction(熟菽, 100)

# Output the result
a#----- content ends here -----

"""
"""
