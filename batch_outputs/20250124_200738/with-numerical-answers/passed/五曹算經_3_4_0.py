"""
今有粟五百六十斛，凡粟八斗易麥五斗。問：得麥㡬何？
術曰：列粟五百六十斛，以五十乘之得二萬八千斛，以八千除之即得。
答曰： a(=350)斛 。
"""

#----- content starts here -----
"""
Suppose there are 560 hu of millet. For every 8 dou of millet, 5 dou of wheat can be exchanged.
Question: how much wheat is obtained?

The procedure says: Place the 560 hu of millet, multiply it by 50, obtaining 28000 dou.
Divide it by 8000, and the result is obtained.

Answer: *a*(=350) hu of wheat.
"""

# 粟五百六十斛
粟 = 560

# 每斛10斗，轉換為斗
粟斗 = 10 * 粟

# 凡粟八斗易麥五斗
粟易麥比 = Fraction(5, 8)

# 以五十乘之得二萬八千斛
實 = 粟斗 * 粟易麥比.numerator

# 以八千除之即得
a = Fraction(實, 粟易麥比.denominator * 10) # 350 hu#----- content ends here -----

"""
"""
