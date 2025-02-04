"""
今有兵一千三百六十二人人給絹二丈八尺五寸問計㡬何
術曰列兵一千三百六十二人以絹二十八尺五寸乘之得三萬八千八百一十七尺以四十尺除之即得
答曰 a疋 
"""

"""
Suppose there are 1362 soldiers, and each is given 2 zhang, 8 chi, and 5 cun of silk.
Question: how much silk in total is required?

The procedure says: Place the 1362 soldiers in a line.
Multiply it by 28 chi and 5 cun (convert to chi first), obtaining 38817 chi.
Divide it by 40 chi (1 bolt of silk is 40 chi), and the result is the number of bolts.

Answer: *a* bolts.
"""

from fractions import Fraction

# 兵一千三百六十二人
兵 = 1362

# 絹二丈八尺五寸 (convert to chi)
丈 = 10  # 1 丈 = 10 尺
尺 = 1   # 1 尺 = 1 尺
寸 = Fraction(1, 10)  # 1 寸 = 1/10 尺

絹每人 = 2 * 丈 + 8 * 尺 + 5 * 寸  # Total silk per person in chi

# 以絹二十八尺五寸乘之
總絹 = 兵 * 絹每人  # Total silk in chi

# 以四十尺除之
疋法 = 40  # 1 疋 = 40 chi
a = Fraction(總絹, 疋法)  # Total bolts of silk

a
"""
"""
