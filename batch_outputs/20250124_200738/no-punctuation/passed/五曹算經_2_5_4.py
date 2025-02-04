"""
今有兵一千三百六十二人人給絹二丈八尺五寸問計㡬何
術曰列兵一千三百六十二人以絹二十八尺五寸乘之得三萬八千八百一十七尺以四十尺除之即得
答曰 a疋 
"""

#----- content starts here -----
"""
Suppose there are 1362 soldiers, and each is given 2 zhang, 8 chi, and 5 cun of silk.
Question: how much silk is needed in total?

The procedure says: Place the 1362 soldiers in a line.
Multiply it by 28 chi and 5 cun of silk, obtaining 38817 chi.
Divide it by 40 chi, obtaining the total number of bolts of silk.

Answer: *a* bolts.
"""

from fractions import Fraction

# 列兵一千三百六十二人
兵 = 1362

# 絹二丈八尺五寸 (convert to chi)
絹每人 = 2 * 10 + 8 + Fraction(5, 10)  # 1 zhang = 10 chi, 1 cun = 1/10 chi

# 以絹二十八尺五寸乘之，得三萬八千八百一十七尺
總絹 = 兵 * 絹每人

# 以四十尺除之，即得
每疋 = 40  # 1 bolt = 40 chi
a = Fraction(總絹, 每疋)  # Total bolts of silk#----- content ends here -----

"""
"""
