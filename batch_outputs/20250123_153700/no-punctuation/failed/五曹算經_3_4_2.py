"""
今有粟五百六十斛凡粟八斗易麥五斗問得麥㡬何
術曰列粟五百六十斛以五十乘之得二萬八千斛以八千除之即得
答曰 a斛 
"""

"""
Suppose there are 560 hu of millet. For every 8 dou of millet, 5 dou of wheat can be exchanged.
Question: how much wheat is obtained?

The procedure says: Place the 560 hu of millet. Multiply it by 50, obtaining 28000 hu. Divide it by 8000, and the result is obtained.

Answer: *a* hu.
"""

# 粟五百六十斛
粟 = 560

# 每8斗粟易5斗麥
# 1斛 = 10斗, so 8斗 = 0.8斛 and 5斗 = 0.5斛
粟率 = Fraction(8, 10)
麥率 = Fraction(5, 10)

# 列粟五百六十斛，以五十乘之
實 = 粟 * 50

# 得二萬八千斛，以八千除之
法 = 8000
a = Fraction(實, 法)
"""
Variable 'a' has wrong value. Expected: 350, Actual: 7/2"""
