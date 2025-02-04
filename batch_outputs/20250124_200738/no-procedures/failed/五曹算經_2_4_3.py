"""
今有兵三千一百四十八人，人給布一丈二尺三寸。問：計㡬何？
答曰： a端 。
"""

#----- content starts here -----
"""
Suppose there are 3,148 soldiers, and each soldier is given 1 zhang, 2 chi, and 3 cun of cloth.
Question: how much cloth is needed in total?

Answer: *a* duan (a bolt of cloth).
"""

# 兵三千一百四十八人
兵 = 3148

# 每人給布一丈二尺三寸
# Convert the cloth given to each soldier into chi (1 zhang = 10 chi, 1 chi = 10 cun)
布每人 = 10 + 2 + Fraction(3, 10)  # 1 zhang = 10 chi, 2 chi, 3 cun = 3/10 chi

# 總布量
總布量 = 兵 * 布每人  # Total cloth in chi

# 每端布長四十丈 (1 duan = 40 zhang = 400 chi)
每端布 = 400  # 1 duan = 400 chi

# 計算總布量需要幾端
a = Fraction(總布量, 每端布)  # Total bolts of cloth needed

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9675051/12500, Actual: 96801/1000"""
