"""
今有粟五百六十斛。問：為糳米㡬何？
答曰： a斛 。
"""

"""
Suppose there are 560 hu of unhusked millet. It is desired to turn it into roughly husked millet.
Question: how much does one obtain?

Answer: it makes *a* hu of roughly husked millet.
"""

from fractions import Fraction

# 粟五百六十斛
粟 = 560

# To convert unhusked millet to husked millet, multiply by 3/5
a = Fraction(3 * 粟, 5)

# Result
a
"""
Variable 'a' has wrong value. Expected: 1344/5, Actual: 336"""
