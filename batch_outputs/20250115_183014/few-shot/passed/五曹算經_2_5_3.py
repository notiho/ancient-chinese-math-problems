"""
今有兵一千三百六十二人，人給絹二丈八尺五寸。問：計㡬何？
術曰：列兵一千三百六十二人，以絹二十八尺五寸乘之，得三萬八千八百一十七尺，以四十尺除之即得。
答曰： a疋 。
"""

"""
Suppose there are 1,362 soldiers, and each soldier is given 2 zhang, 8 chi, and 5 cun of silk.
Question: how much silk is needed in total?

The procedure says: Place the 1,362 soldiers, and multiply it by 28 chi and 5 cun (converted to chi), obtaining 38,817 chi.
Divide this by 40 chi (1 bolt of silk) to get the total number of bolts.

Answer: *a* bolts.
"""

# 列兵一千三百六十二人
兵 = 1362

# 絹二丈八尺五寸 (convert to chi)
丈 = 10  # 1 丈 = 10 尺
尺 = 1   # 1 尺 = 1 尺
寸 = Fraction(1, 10)  # 1 寸 = 1/10 尺

絹每人 = 2 * 丈 + 8 * 尺 + 5 * 寸  # Convert to total chi

# 以絹二十八尺五寸乘之
總絹 = 兵 * 絹每人  # Total chi of silk

# 以四十尺除之即得
每疋 = 40  # 1 疋 = 40 chi
a = Fraction(總絹, 每疋)  # Total bolts of silk
"""
"""
