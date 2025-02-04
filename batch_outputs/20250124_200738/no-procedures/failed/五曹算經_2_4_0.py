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
# Convert the cloth per person into chi (1 zhang = 10 chi, 1 chi = 10 cun)
布每人 = 10 + 2 + Fraction(3, 10)  # 1 zhang = 10 chi, 2 chi, 3 cun = 3/10 chi

# 計算總布量 (in chi)
總布量 = 兵 * 布每人

# 每端布為五十丈 (1 duan = 50 zhang = 500 chi)
每端布 = 500  # 50 zhang = 500 chi

# 計算需要的端數
a = Fraction(總布量, 每端布)  # Total cloth divided by cloth per bolt (duan)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9675051/12500, Actual: 96801/1250"""
