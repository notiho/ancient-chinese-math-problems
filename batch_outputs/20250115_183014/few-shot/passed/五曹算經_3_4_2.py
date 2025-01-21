"""
今有粟五百六十斛，凡粟八斗易麥五斗。問：得麥㡬何？
術曰：列粟五百六十斛，以五十乘之得二萬八千斛，以八千除之即得。
答曰： a斛 。
"""

"""
Suppose there are 560 hu of millet. For every 8 dou of millet, 5 dou of wheat can be exchanged.
Question: how much wheat is obtained?

The procedure says: Place the 560 hu of millet, multiply it by 50, obtaining 28000 hu.
Divide it by 8000, and the result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 粟五百六十斛
粟 = 560

# 每斛有10斗
粟斗 = 10 * 粟

# 凡粟八斗易麥五斗
粟易率 = 8
麥得率 = 5

# 以五十乘之得二萬八千斛
實 = 粟斗 * 麥得率

# 以八千除之即得
法 = 粟易率
a = Fraction(實, 法) / 10  # Convert back to hu from dou
"""
"""
