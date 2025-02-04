"""
今有粟五百六十斛，凡粟八斗易麥五斗。問：得麥㡬何？
術曰：列粟五百六十斛，以五十乘之得二萬八千斛，以八千除之即得。
答曰： a斛 。
"""

"""
Suppose there are 560 hu of millet, and for every 8 dou of millet, 5 dou of wheat can be exchanged.
Question: how much wheat is obtained?

The procedure says: Place the 560 hu of millet, multiply it by 50, obtaining 28000 dou.
Divide it by 8000, and the result is obtained.

Answer: *a* hu.
"""

# 粟五百六十斛
粟 = 560

# 每斛十斗，轉換為斗
粟斗 = 10 * 粟

# 以五十乘之得二萬八千斗
實 = 50 * 粟斗

# 每八斗粟易五斗麥，八千為法
法 = 8 * 1000

# 以八千除之即得
麥斗 = Fraction(實, 法)

# 每十斗為一斛，轉換為斛
a = 麥斗 / 10
"""
Variable 'a' has wrong value. Expected: 350, Actual: 7/2"""
