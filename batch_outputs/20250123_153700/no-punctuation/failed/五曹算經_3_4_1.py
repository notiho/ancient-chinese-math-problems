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

# 每8斗易5斗
# Convert the exchange rate to a multiplier for hu (1 hu = 10 dou)
交換率 = Fraction(5, 8)

# 粟以五十乘之
實 = 粟 * 50

# 得二萬八千斛
實 = 28000  # Confirmed from the procedure

# 以八千除之
a = Fraction(實, 8000)
"""
Variable 'a' has wrong value. Expected: 350, Actual: 7/2"""
