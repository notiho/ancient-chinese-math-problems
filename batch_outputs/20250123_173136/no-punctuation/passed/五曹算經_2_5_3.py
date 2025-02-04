"""
今有兵一千三百六十二人人給絹二丈八尺五寸問計㡬何
術曰列兵一千三百六十二人以絹二十八尺五寸乘之得三萬八千八百一十七尺以四十尺除之即得
答曰 a疋 
"""

"""
Suppose there are 1362 soldiers, and each is given 2 zhang, 8 chi, and 5 cun of silk.
Question: how much silk is needed in total?

The procedure says: List the 1362 soldiers.
Take the silk of 28 chi and 5 cun, multiply it by the number of soldiers, obtaining 38817 chi.
Divide it by 40 chi (1 bolt of silk), and the result is the number of bolts.

Answer: *a* bolts.
"""

from fractions import Fraction

# 兵一千三百六十二人
兵 = 1362

# 絹二丈八尺五寸 (convert to chi)
絹 = 2 * 10 + 8 + Fraction(5, 10)

# 以絹乘兵，得總尺數
總尺數 = 絹 * 兵

# 一疋四十尺
疋尺數 = 40

# 以四十尺除之，即得疋數
a = Fraction(總尺數, 疋尺數)
"""
"""
