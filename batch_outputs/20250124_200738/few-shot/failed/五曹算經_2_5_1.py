"""
今有兵一千三百六十二人，人給絹二丈八尺五寸。問：計㡬何？
術曰：列兵一千三百六十二人，以絹二十八尺五寸乘之，得三萬八千八百一十七尺，以四十尺除之即得。
答曰： a疋 。
"""

#----- content starts here -----
"""
Suppose there are 1,362 soldiers, and each soldier is given 2 zhang, 8 chi, and 5 cun of silk.
Question: how much silk is required in total?

The procedure says: Place the 1,362 soldiers, and multiply by 28 chi and 5 cun (convert to chi as 28.5 chi), obtaining 38,817 chi.
Divide by 40 chi (the length of one bolt of silk), and the result is the number of bolts.

Answer: *a* bolts.
"""

# 列兵一千三百六十二人
兵 = 1362

# 絹二丈八尺五寸 (convert to chi: 1 zhang = 10 chi, 1 cun = 0.1 chi)
絹每人 = 2 * 10 + 8 + 0.5  # 2 zhang + 8 chi + 5 cun = 28.5 chi

# 以絹二十八尺五寸乘之
總絹 = 兵 * 絹每人  # Total chi of silk

# 得三萬八千八百一十七尺 (verification step)
assert 總絹 == 38817  # Ensure the calculation matches the problem statement

# 以四十尺除之即得 (1 bolt = 40 chi)
a = Fraction(總絹, 40)  # Total bolts of silk#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
