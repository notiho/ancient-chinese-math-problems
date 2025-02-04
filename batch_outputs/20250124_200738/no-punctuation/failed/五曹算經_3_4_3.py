"""
今有粟五百六十斛凡粟八斗易麥五斗問得麥㡬何
術曰列粟五百六十斛以五十乘之得二萬八千斛以八千除之即得
答曰 a斛 
"""

#----- content starts here -----
"""
Suppose there are 560 hu of millet. For every 8 dou of millet, 5 dou of wheat is exchanged.
Question: how much wheat is obtained?

The procedure says: Place the 560 hu of millet, multiply it by 50, obtaining 28000 hu.
Divide it by 8000, and the result is obtained.

Answer: *a* hu.
"""

# 粟五百六十斛
粟 = 560

# 每斛有10斗
粟斗 = 10 * 粟

# 每8斗粟易5斗麥
粟兌換率 = 8
麥兌換率 = 5

# 以五十乘之
實 = 50 * 粟斗

# 得二萬八千斛，以八千除之
a = Fraction(實, 8000)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 350, Actual: 35"""
