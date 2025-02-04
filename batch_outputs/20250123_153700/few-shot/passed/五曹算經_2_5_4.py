"""
今有兵一千三百六十二人，人給絹二丈八尺五寸。問：計㡬何？
術曰：列兵一千三百六十二人，以絹二十八尺五寸乘之，得三萬八千八百一十七尺，以四十尺除之即得。
答曰： a疋 。
"""

"""
Suppose there are 1362 soldiers, and each soldier is given 2 zhang 8 chi 5 cun of silk.
Question: how much silk is needed in total?

The procedure says: Place the 1362 soldiers, and multiply by 28 chi 5 cun of silk (convert to chi first), obtaining 38817 chi.
Divide by 40 chi (1 bolt of silk = 40 chi), and the result is the number of bolts.

Answer: *a* bolts.
"""

# 列兵一千三百六十二人
兵 = 1362

# 絹二丈八尺五寸
# Convert to chi: 1 zhang = 10 chi, 1 cun = 1/10 chi
絹 = 2 * 10 + 8 + Fraction(5, 10)  # 絹 in chi

# 以絹二十八尺五寸乘之
總絹 = 兵 * 絹  # Total silk in chi

# 以四十尺除之即得
a = Fraction(總絹, 40)  # Convert to bolts of silk
"""
"""
