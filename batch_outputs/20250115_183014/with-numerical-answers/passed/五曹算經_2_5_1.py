"""
今有兵一千三百六十二人，人給絹二丈八尺五寸。問：計㡬何？
術曰：列兵一千三百六十二人，以絹二十八尺五寸乘之，得三萬八千八百一十七尺，以四十尺除之即得。
答曰： a(=38817/40)疋 。
"""

"""
Suppose there are 1362 soldiers, and each soldier is given 2 zhang, 8 chi, and 5 cun of silk.
Question: how much silk is needed in total?

The procedure says: Place the 1362 soldiers in a line.
Multiply by 28 chi and 5 cun of silk, obtaining 38817 chi.
Divide by 40 chi to get the number of bolts of silk.

Answer: *a*(=38817/40) bolts of silk.
"""

from fractions import Fraction

# 兵一千三百六十二人
兵 = 1362

# 人給絹二丈八尺五寸
# Convert to chi (1 zhang = 10 chi, 1 cun = 1/10 chi)
絹 = 2 * 10 + 8 + Fraction(5, 10)  # 28.5 chi

# 以絹二十八尺五寸乘之，得三萬八千八百一十七尺
總尺 = 兵 * 絹  # 38817 chi

# 以四十尺除之即得
a = Fraction(總尺, 40)  # 38817/40 bolts of silk
"""
"""
