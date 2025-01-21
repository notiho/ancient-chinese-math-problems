"""
今有粟五百六十斛凡粟八斗易麥五斗問得麥㡬何
術曰列粟五百六十斛以五十乘之得二萬八千斛以八千除之即得
答曰 a斛 
"""

"""
Suppose there are 560 hu of millet. For every 8 dou of millet, 5 dou of wheat can be exchanged.
Question: how much wheat is obtained?

The procedure says: Place the 560 hu of millet, multiply it by 50, obtaining 28000 hu.
Divide it by 8000, and the result is the amount of wheat.

The answer says: *a* hu.
"""

# 粟五百六十斛
粟 = 560

# 每斛有十斗，轉換為斗
粟斗 = 10 * 粟

# 每八斗粟易五斗麥
粟換率 = 8
麥換率 = 5

# 列粟五百六十斛，以五十乘之
實 = 粟斗 * 麥換率

# 得二萬八千斛，以八千除之
a = Fraction(實, 粟換率) / 10  # Convert back to hu
"""
"""
