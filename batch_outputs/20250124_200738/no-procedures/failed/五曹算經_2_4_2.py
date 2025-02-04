"""
今有兵三千一百四十八人，人給布一丈二尺三寸。問：計㡬何？
答曰： a端 。
"""

#----- content starts here -----
"""
Suppose there are 3,148 soldiers, and each soldier is given 1 zhang, 2 chi, and 3 cun of cloth.
Question: how much cloth is needed in total?

Answer: *a* duan (a unit of cloth measurement).
"""

# Total number of soldiers
兵 = 3148

# Cloth given to each soldier: 1丈2尺3寸
# Convert to chi (1丈 = 10尺, 1尺 = 10寸)
布_per_兵 = 10 + 2 + Fraction(3, 10)  # Total in chi

# Total cloth needed in chi
總布_in_尺 = 兵 * 布_per_兵

# Convert chi to duan (1端 = 40 chi)
a = Fraction(總布_in_尺, 40)  # Total in duan#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9675051/12500, Actual: 96801/100"""
