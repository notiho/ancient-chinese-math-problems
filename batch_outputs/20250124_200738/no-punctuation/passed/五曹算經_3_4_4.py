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

# 每八斗易五斗
# Convert 8 dou and 5 dou into hu (1 hu = 10 dou)
粟換率 = 8 / 10  # 8 dou of millet in hu
麥換率 = 5 / 10  # 5 dou of wheat in hu

# 列粟五百六十斛，以五十乘之
實 = 粟 * (麥換率 / 粟換率)  # Multiply by the exchange ratio (5/8)

# 答曰
a = Fraction(實).limit_denominator()  # Ensure the result is in fractional form if necessary#----- content ends here -----

"""
"""
