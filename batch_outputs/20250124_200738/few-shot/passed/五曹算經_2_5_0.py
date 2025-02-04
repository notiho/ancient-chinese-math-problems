"""
今有兵一千三百六十二人，人給絹二丈八尺五寸。問：計㡬何？
術曰：列兵一千三百六十二人，以絹二十八尺五寸乘之，得三萬八千八百一十七尺，以四十尺除之即得。
答曰： a疋 。
"""

#----- content starts here -----
"""
Suppose there are 1,362 soldiers, and each soldier is given 2 zhang, 8 chi, and 5 cun of silk.
Question: how much silk is needed in total?

The procedure says: Place the 1,362 soldiers, and multiply by 28 chi and 5 cun (convert to chi).
This gives 38,817 chi.
Divide by 40 chi (1 bolt of silk = 40 chi), and the result is the number of bolts of silk.

Answer: *a* bolts.
"""

# 列兵一千三百六十二人
兵 = 1362

# 絹二丈八尺五寸 (convert to chi)
丈 = 10  # 1 丈 = 10 尺
尺 = 1   # 1 尺 = 1 尺
寸 = Fraction(1, 10)  # 1 寸 = 1/10 尺

絹每人 = (2 * 丈) + (8 * 尺) + (5 * 寸)

# 以絹二十八尺五寸乘之
總絹尺 = 兵 * 絹每人

# 以四十尺除之即得
每疋 = 40  # 1 疋 = 40 尺
a = Fraction(總絹尺, 每疋)  # 絹的總疋數#----- content ends here -----

"""
"""
