"""
今有兵一千三百六十二人，人給絹二丈八尺五寸。問：計㡬何？
術曰：列兵一千三百六十二人，以絹二十八尺五寸乘之，得三萬八千八百一十七尺，以四十尺除之即得。
答曰： a(=38817/40)疋 。
"""

#----- content starts here -----
"""
Suppose there are 1,362 soldiers, and each soldier is given 2 zhang, 8 chi, and 5 cun of silk.
Question: how much silk is needed in total?

The procedure says: Place the 1,362 soldiers in a line.
Multiply by 28 chi and 5 cun of silk, obtaining 38,817 chi.
Divide by 40 chi to obtain the number of bolts of silk.

Answer: *a*(=38817/40) bolts of silk.
"""

from fractions import Fraction

# 兵一千三百六十二人
兵 = 1362

# 人給絹二丈八尺五寸
# Convert to 尺 (1 丈 = 10 尺, 1 尺 = 10 寸)
絹每人 = 2 * 10 + 8 + Fraction(5, 10)  # 28 尺 5 寸 = 28 + 5/10 = 28.5 尺

# 以絹二十八尺五寸乘之，得三萬八千八百一十七尺
總絹尺 = 兵 * 絹每人  # 38817 尺

# 以四十尺除之即得
每疋尺 = 40
a = Fraction(總絹尺, 每疋尺)  # 38817/40 疋#----- content ends here -----

"""
"""
