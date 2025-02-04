"""
今有兵一千三百六十二人，人給絹二丈八尺五寸。問：計㡬何？
術曰：列兵一千三百六十二人，以絹二十八尺五寸乘之，得三萬八千八百一十七尺，以四十尺除之即得。
答曰： a(=38817/40)疋 。
"""

"""
Suppose there are 1362 soldiers. Each soldier is given 2 zhang, 8 chi, and 5 cun of silk.
Question: how much silk is needed in total?

The procedure says: Place the 1362 soldiers in a line. Multiply by 28 chi and 5 cun of silk, obtaining 38817 chi.
Divide by 40 chi to get the number of bolts of silk.

Answer: *a*(=38817/40) bolts of silk.
"""

from fractions import Fraction

# 兵一千三百六十二人
兵 = 1362

# 每人給絹二丈八尺五寸
# Convert to chi (1 zhang = 10 chi, 1 cun = 1/10 chi)
每人絹 = 2 * 10 + 8 + Fraction(5, 10)  # 28.5 chi

# 以絹二十八尺五寸乘之
總絹尺 = 兵 * 每人絹  # 38817 chi

# 以四十尺除之即得
每疋尺 = 40
a = Fraction(總絹尺, 每疋尺)  # 38817/40 bolts of silk
"""
"""
