"""
今有兵一千三百六十二人，人給絹二丈八尺五寸。問：計㡬何？
答曰： a疋 。
"""

#----- content starts here -----
"""
Suppose there are 1,362 soldiers, and each soldier is given 2 zhang, 8 chi, and 5 cun of silk.
Question: how much silk is needed in total?

Answer: *a* bolts of silk.
"""

# Define the number of soldiers
兵 = 1362

# Define the amount of silk given to each soldier in chi (1 zhang = 10 chi, 1 cun = 1/10 chi)
每人絹 = 2 * 10 + 8 + Fraction(5, 10)  # Convert to chi

# Total silk needed in chi
總絹 = 兵 * 每人絹

# Convert chi to bolts of silk (1 bolt = 50 chi)
a = Fraction(總絹, 50)

a  # Output the total number of bolts of silk needed#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 38817/40, Actual: 38817/50"""
