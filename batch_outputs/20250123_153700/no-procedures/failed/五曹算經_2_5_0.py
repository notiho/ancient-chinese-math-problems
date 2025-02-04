"""
今有兵一千三百六十二人，人給絹二丈八尺五寸。問：計㡬何？
答曰： a疋 。
"""

"""
Suppose there are 1,362 soldiers, and each soldier is given 2 zhang, 8 chi, and 5 cun of silk.
Question: how much silk is needed in total?

Answer: *a* bolts of silk.
"""

# 兵一千三百六十二人
兵 = 1362

# 每人給絹二丈八尺五寸
# Convert the given silk per person into chi (1 zhang = 10 chi, 1 chi = 10 cun)
絹每人 = 2 * 10 + 8 + Fraction(5, 10)  # Convert to chi

# 計總共需要的絹 (in chi)
總絹 = 兵 * 絹每人

# Convert chi into bolts of silk (1 bolt = 50 chi)
a = Fraction(總絹, 50)

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 38817/40, Actual: 38817/50"""
