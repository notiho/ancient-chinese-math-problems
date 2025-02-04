"""
今有兵一千三百六十二人人給絹二丈八尺五寸問計㡬何
術曰列兵一千三百六十二人以絹二十八尺五寸乘之得三萬八千八百一十七尺以四十尺除之即得
答曰 a疋 
"""

#----- content starts here -----
"""
Suppose there are 1,362 soldiers, and each is given 2 zhang, 8 chi, and 5 cun of silk.
Question: how many bolts of silk are required in total?

The procedure says: Place the 1,362 soldiers in a line.
Multiply by 28 chi and 5 cun of silk, obtaining 38,817 chi.
Divide by 40 chi, obtaining the number of bolts.

Answer: *a* bolts.
"""

from fractions import Fraction

# 列兵一千三百六十二人
兵 = 1362

# 絹二丈八尺五寸 (convert to chi)
絹 = 2 * 10 + 8 + Fraction(5, 10)  # 1 zhang = 10 chi, 1 cun = 1/10 chi

# 以絹二十八尺五寸乘之，得三萬八千八百一十七尺
總尺 = 兵 * 絹

# 以四十尺除之，即得
每疋尺 = 40
a = Fraction(總尺, 每疋尺)  # Number of bolts of silk#----- content ends here -----

"""
"""
