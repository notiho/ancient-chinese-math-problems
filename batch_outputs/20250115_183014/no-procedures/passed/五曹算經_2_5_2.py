"""
今有兵一千三百六十二人，人給絹二丈八尺五寸。問：計㡬何？
答曰： a疋 。
"""

"""
Suppose there are 1,362 soldiers, and each soldier is given 2 zhang, 8 chi, and 5 cun of silk.
Question: how much silk is needed in total?

Answer: *a* bolts of silk.
"""

# Total number of soldiers
兵 = 1362

# Silk given to each soldier in zhang, chi, and cun
每人絹 = 2 * 10 + 8 + Fraction(5, 10)  # Convert to chi (1 zhang = 10 chi, 1 chi = 10 cun)

# Total silk required in chi
總絹 = 兵 * 每人絹

# Convert chi to bolts of silk (1 bolt = 40 chi)
a = Fraction(總絹, 40)  # Total bolts of silk required

a  # Output the result
"""
"""
