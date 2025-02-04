"""
今有兵一千三百六十二人，人給絹二丈八尺五寸。問：計㡬何？
答曰： a疋 。
"""

#----- content starts here -----
"""
Suppose there are 1,362 soldiers, and each soldier is given 2 zhang, 8 chi, and 5 cun of silk.  
Question: how much silk is needed in total?

Answer: *a* bolts of silk (疋).
"""

# 兵一千三百六十二人
兵 = 1362

# 每人給絹二丈八尺五寸
# Convert the silk length to chi (1 zhang = 10 chi, 1 cun = 1/10 chi)
每人絹 = 2 * 10 + 8 + Fraction(5, 10)  # 2 zhang + 8 chi + 5 cun

# 計算總長度 (in chi)
總長度 = 兵 * 每人絹

# 每疋絹為40丈 (1 疋 = 40 zhang = 400 chi)
每疋絹 = 40 * 10  # 40 zhang in chi

# 計算所需疋數
a = Fraction(總長度, 每疋絹)

# Answer: a疋
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 38817/40, Actual: 38817/400"""
