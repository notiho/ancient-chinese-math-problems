"""
今有兵一千三百六十二人，人給絹二丈八尺五寸。問：計㡬何？
術曰：列兵一千三百六十二人，以絹二十八尺五寸乘之，得三萬八千八百一十七尺，以四十尺除之即得。
答曰： a疋 。
"""

#----- content starts here -----
"""
Suppose there are 1,362 soldiers, and each soldier is given 2 zhang, 8 chi, and 5 cun of silk.
Question: how much silk is needed in total?

The procedure says: Place the number of soldiers, 1,362, and multiply it by the silk length of 28 chi and 5 cun (converted to chi as 28.5 chi), obtaining the total length in chi.
Divide the total length by 40 chi (the length of one bolt of silk), and the result is the number of bolts.

Answer: *a* bolts of silk.
"""

from fractions import Fraction

# 兵一千三百六十二人
兵 = 1362

# 每人給絹二丈八尺五寸
# Convert to chi: 1 zhang = 10 chi, 1 cun = 1/10 chi
絹每人 = 2 * 10 + 8 + Fraction(5, 10)  # 2 zhang + 8 chi + 5 cun

# 總絹長度 (in chi)
總絹長度 = 兵 * 絹每人

# 每疋絹長度為 40 chi
每疋絹長度 = 40

# 計算疋數
a = Fraction(總絹長度, 每疋絹長度)

# Output the result
a#----- content ends here -----

"""
"""
