"""
今有粟七百五十斛。問：為糲米㡬何？
答曰： a斛 。
"""

"""
Suppose there are 750 hu of unhusked millet. It is desired to turn it into roughly husked millet.
Question: how much does one obtain?

The answer says: *a* hu of roughly husked millet.
"""

# 粟七百五十斛
粟 = 750

# Multiply by 3 and divide by 5 to get husked millet
a = Fraction(3 * 粟, 5)

# Result
a
"""
"""
