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
粟易率 = 8
麥得率 = 5

# 以五十乘之得二萬八千斛
實 = 50 * 粟斗

# 以八千除之即得
a = Fraction(實, 8000) # 350 hu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 350, Actual: 35"""
