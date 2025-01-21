"""
今有粟五百六十斛問為糳米㡬何
術曰列粟五百六十斛以二十四乘之得一萬三千四百四十斛以五十除之即得
答曰 a斛 
"""

"""
Suppose there are 560 hu of unhusked millet.
Question: how much roughly husked millet does it make?

The procedure says: Place the 560 hu of millet.
Multiply it by 24, obtaining 13440 hu.
Divide it by 50, and the result is obtained.

Answer: *a* hu.
"""

# 粟五百六十斛
粟 = 560

# 以二十四乘之
實 = 24 * 粟

# 以五十除之
a = Fraction(實, 50)
"""
"""
