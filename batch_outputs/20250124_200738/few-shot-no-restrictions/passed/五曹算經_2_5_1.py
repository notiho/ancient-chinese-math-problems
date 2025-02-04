"""
今有兵一千三百六十二人，人給絹二丈八尺五寸。問：計㡬何？
術曰：列兵一千三百六十二人，以絹二十八尺五寸乘之，得三萬八千八百一十七尺，以四十尺除之即得。
答曰： a疋 。
"""

#----- content starts here -----
"""
Suppose there are 1,362 soldiers, and each soldier is given 2 zhang, 8 chi, and 5 cun of silk.
Question: how much silk is needed in total?

The procedure says: Place the 1,362 soldiers, and multiply it by 28 chi and 5 cun (convert zhang, chi, and cun into chi). 
This gives the total number of chi. 
Divide the total by 40 chi (1 bolt of silk = 40 chi), and the result is the number of bolts of silk.

Answer: *a* bolts.
"""

from fractions import Fraction

# 兵一千三百六十二人
兵 = 1362

# 每人給絹二丈八尺五寸
# 1 丈 = 10 尺, 1 尺 = 10 寸
每人絹 = 2 * 10 + 8 + Fraction(5, 10)  # Convert to 尺

# 總絹數 (以尺為單位)
總絹數 = 兵 * 每人絹

# 每疋絹為 40 尺
每疋絹 = 40

# 計算疋數
a = Fraction(總絹數, 每疋絹)

# Output the result
a#----- content ends here -----

"""
"""
