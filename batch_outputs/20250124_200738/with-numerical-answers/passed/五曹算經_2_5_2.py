"""
今有兵一千三百六十二人，人給絹二丈八尺五寸。問：計㡬何？
術曰：列兵一千三百六十二人，以絹二十八尺五寸乘之，得三萬八千八百一十七尺，以四十尺除之即得。
答曰： a(=38817/40)疋 。
"""

#----- content starts here -----
"""
Suppose there are 1362 soldiers, and each soldier is given 2 zhang, 8 chi, and 5 cun of silk.
Question: how much silk in total is required?

The procedure says: Place the 1362 soldiers in a line. Multiply by the silk amount of 28 chi and 5 cun, obtaining 38817 chi. 
Divide this by 40 chi to get the number of bolts of silk.

Answer: *a*(=38817/40) bolts of silk.
"""

from fractions import Fraction

# 兵一千三百六十二人
兵 = 1362

# 人給絹二丈八尺五寸
丈 = 10  # 1 丈 = 10 尺
尺 = 1   # 1 尺 = 1 尺
寸 = Fraction(1, 10)  # 1 寸 = 1/10 尺

絹每人 = 2 * 丈 + 8 * 尺 + 5 * 寸  # Convert to 尺

# 以絹二十八尺五寸乘之
總絹尺 = 兵 * 絹每人

# 以四十尺除之即得
每疋尺 = 40  # 1 疋 = 40 尺
a = Fraction(總絹尺, 每疋尺)  # 38817/40 bolts of silk#----- content ends here -----

"""
"""
