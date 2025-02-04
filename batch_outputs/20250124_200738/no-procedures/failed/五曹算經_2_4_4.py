"""
今有兵三千一百四十八人，人給布一丈二尺三寸。問：計㡬何？
答曰： a端 。
"""

#----- content starts here -----
"""
Suppose there are 3,148 soldiers, and each soldier is given 1 zhang, 2 chi, and 3 cun of cloth.
Question: how much total cloth is required?

Answer: *a* duan (a bolt of cloth).
"""

# 兵三千一百四十八人
兵 = 3148

# 每人給布一丈二尺三寸
# Convert 1 zhang, 2 chi, 3 cun into chi (1 zhang = 10 chi, 1 chi = 10 cun)
布_per_人 = 10 + 2 + Fraction(3, 10)  # Total in chi

# 總布量
總布量 = 兵 * 布_per_人  # Total cloth in chi

# 每端布長 50 chi (1 duan = 50 chi)
a = Fraction(總布量, 50)  # Total bolts of cloth required#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9675051/12500, Actual: 96801/125"""
