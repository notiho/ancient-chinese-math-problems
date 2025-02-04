"""
今有粟一斗，欲為小䵂。問︰得幾何？
術曰：以粟求小䵂，二十七之，百而一。
荅曰：為小䵂 a升 。
"""

#----- content starts here -----
"""
Suppose there is one dou of millet. It is desired to turn it into xiao mi (small husked rice).
Question: how much does one obtain?

The procedure says: when seeking xiao mi from millet, multiply by 27 and divide by 100.

The answer says: it makes *a* sheng of xiao mi.
"""

from fractions import Fraction

# 粟一斗
粟 = 1  # in dou

# Convert dou to sheng (1 dou = 10 sheng)
粟 = 10 * 粟  # in sheng

# 以粟求小䵂，二十七之
小䵂 = 27 * 粟

# 百而一
a = Fraction(小䵂, 100)

# Output the result
a#----- content ends here -----

"""
"""
