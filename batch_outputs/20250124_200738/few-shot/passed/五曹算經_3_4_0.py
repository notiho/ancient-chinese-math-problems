"""
今有粟五百六十斛，凡粟八斗易麥五斗。問：得麥㡬何？
術曰：列粟五百六十斛，以五十乘之得二萬八千斛，以八千除之即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 560 hu of millet, and in general, 8 dou of millet can be exchanged for 5 dou of wheat.
Question: how much wheat is obtained?

The procedure says: Place the 560 hu of millet, multiply it by 50, obtaining 28000 dou.
Divide it by 8000, and the result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 粟五百六十斛
粟 = 560

# 1斛 = 10斗, convert 粟 to 斗
粟斗 = 10 * 粟

# 凡粟八斗易麥五斗
粟兌換率 = 8
麥兌換率 = 5

# 列粟五百六十斛，以五十乘之得二萬八千斛
實 = 粟斗 * 麥兌換率

# 以八千除之即得
法 = 粟兌換率
麥斗 = Fraction(實, 法)

# Convert 麥斗 back to 斛 (1斛 = 10斗)
a = 麥斗 / 10#----- content ends here -----

"""
"""
