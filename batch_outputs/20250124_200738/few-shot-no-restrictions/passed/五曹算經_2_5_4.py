"""
今有兵一千三百六十二人，人給絹二丈八尺五寸。問：計㡬何？
術曰：列兵一千三百六十二人，以絹二十八尺五寸乘之，得三萬八千八百一十七尺，以四十尺除之即得。
答曰： a疋 。
"""

#----- content starts here -----
"""
Suppose there are 1,362 soldiers, and each soldier is given 2 zhang, 8 chi, and 5 cun of silk.
Question: how much silk is needed in total?

The procedure says: Place the 1,362 soldiers, and multiply by the silk amount of 28 chi and 5 cun (converted to chi).
This gives the total amount in chi. Divide this by 40 chi (the length of one bolt of silk) to get the number of bolts.

Answer: *a* bolts.
"""

from fractions import Fraction

# 兵一千三百六十二人
兵 = 1362

# 每人給絹二丈八尺五寸
# Convert to chi (1 zhang = 10 chi, 1 cun = 1/10 chi)
絹每人 = 2 * 10 + 8 + Fraction(5, 10)  # 2 zhang, 8 chi, 5 cun

# 總計絹的尺數
總絹尺數 = 兵 * 絹每人

# 一疋等於四十尺
疋長度 = 40

# 計算疋數
a = Fraction(總絹尺數, 疋長度)

# Output
a#----- content ends here -----

"""
"""
