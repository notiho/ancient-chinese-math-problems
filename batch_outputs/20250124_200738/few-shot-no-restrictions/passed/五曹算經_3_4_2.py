"""
今有粟五百六十斛，凡粟八斗易麥五斗。問：得麥㡬何？
術曰：列粟五百六十斛，以五十乘之得二萬八千斛，以八千除之即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 560 hu of millet. For every 8 dou of millet, 5 dou of wheat can be exchanged.
Question: how much wheat can be obtained?

The procedure says: Place the 560 hu of millet. Multiply it by 50, obtaining 28000 dou. Divide it by 8, obtaining the result.

Answer: *a* hu.
"""

from fractions import Fraction

# 粟五百六十斛
粟 = 560  # in hu

# 1 hu = 10 dou, convert 粟 to dou
粟斗 = 10 * 粟

# 凡粟八斗易麥五斗
粟兌換率 = 8  # 8 dou of millet
麥兌換率 = 5  # 5 dou of wheat

# 以五十乘之
實 = 粟斗 * 麥兌換率

# 以八千除之即得
a斗 = Fraction(實, 粟兌換率)

# Convert result back to hu (1 hu = 10 dou)
a = a斗 / 10  # in hu

a  # Answer in hu#----- content ends here -----

"""
"""
