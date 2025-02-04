"""
今有粟七百五十斛。問：為糲米㡬何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 750 hu of unhusked millet. It is desired to turn it into roughly husked millet.
Question: how much husked millet does it make?

Answer: it makes *a* hu.
"""

from fractions import Fraction

# 粟七百五十斛
粟 = 750

# To convert unhusked millet to husked millet, multiply by 3/5
a = Fraction(3 * 粟, 5)

# Result
a#----- content ends here -----

"""
"""
