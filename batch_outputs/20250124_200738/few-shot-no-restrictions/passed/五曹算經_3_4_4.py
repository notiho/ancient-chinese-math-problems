"""
今有粟五百六十斛，凡粟八斗易麥五斗。問：得麥㡬何？
術曰：列粟五百六十斛，以五十乘之得二萬八千斛，以八千除之即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 560 hu of millet, and every 8 dou of millet can be exchanged for 5 dou of wheat.
Question: how much wheat can be obtained?

The procedure says: Place the 560 hu of millet, multiply it by 50, obtaining 28,000 dou.
Divide it by 8,000, and the result is the amount of wheat.

Answer: *a* hu.
"""

from fractions import Fraction

# 粟五百六十斛
粟 = 560  # in hu

# 每斛有10斗
粟斗 = 10 * 粟  # convert hu to dou

# 凡粟八斗易麥五斗
粟兌換率 = 8  # 8 dou of millet
麥兌換率 = 5  # 5 dou of wheat

# 以五十乘之
實 = 粟斗 * 麥兌換率

# 以八千除之
法 = 粟兌換率

# 得麥
麥斗 = Fraction(實, 法)

# Convert back to hu (10 dou = 1 hu)
a = 麥斗 / 10  # in hu

a#----- content ends here -----

"""
"""
