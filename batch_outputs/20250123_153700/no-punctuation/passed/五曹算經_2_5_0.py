"""
今有兵一千三百六十二人人給絹二丈八尺五寸問計㡬何
術曰列兵一千三百六十二人以絹二十八尺五寸乘之得三萬八千八百一十七尺以四十尺除之即得
答曰 a疋 
"""

"""
Suppose there are 1,362 soldiers, and each is given 2 zhang, 8 chi, and 5 cun of silk.
Question: how much silk is needed in total?

The procedure says: Place the 1,362 soldiers in a line.
Multiply it by 28 chi and 5 cun of silk, obtaining 38,817 chi.
Divide this by 40 chi, obtaining the total number of bolts of silk.

Answer: *a* bolts.
"""

from fractions import Fraction

# 列兵一千三百六十二人
兵 = 1362

# 絹二丈八尺五寸
# Convert to chi (1 丈 = 10 尺, 1 尺 = 10 寸)
絹每人 = 2 * 10 + 8 + Fraction(5, 10)

# 以絹二十八尺五寸乘之
總絹尺 = 兵 * 絹每人

# 得三萬八千八百一十七尺
assert 總絹尺 == 38817  # Confirm the intermediate result matches the problem

# 以四十尺除之
疋法 = 40
a = Fraction(總絹尺, 疋法)  # Total bolts of silk
"""
"""
