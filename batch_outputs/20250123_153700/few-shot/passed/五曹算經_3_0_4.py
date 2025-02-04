"""
今有粟七百五十斛。問：為糲米㡬何？
術曰：列粟七百五十斛，以三十乘之得二萬二千五百斛，以五十除之即得。
答曰： a斛 。
"""

"""
Suppose there are 750 hu of unhusked millet.
Question: how much roughly husked millet does it make?

The procedure says: Place the 750 hu of millet.
Multiply it by 30, obtaining 22,500 hu.
Divide it by 50, and the result is obtained.

Answer: *a* hu.
"""

# 粟七百五十斛
粟 = 750

# 以三十乘之
實 = 30 * 粟

# 以五十除之即得
a = Fraction(實, 50)
"""
"""
