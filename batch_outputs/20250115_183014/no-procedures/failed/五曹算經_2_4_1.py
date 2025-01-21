"""
今有兵三千一百四十八人，人給布一丈二尺三寸。問：計㡬何？
答曰： a端 。
"""

"""
Suppose there are 3,148 soldiers, and each soldier is given 1 zhang, 2 chi, and 3 cun of cloth.
Question: how much cloth is needed in total?

Answer: *a* duan (a unit of cloth measurement).
"""

# 兵三千一百四十八人
兵 = 3148

# 每人給布一丈二尺三寸
# Convert the cloth length to chi (1 zhang = 10 chi, 1 chi = 10 cun)
布_每人 = 10 + 2 + Fraction(3, 10)  # 1 zhang = 10 chi, 2 chi, 3 cun = 3/10 chi

# 總布量
總布量 = 兵 * 布_每人

# Convert the total cloth into duan (1 duan = 50 chi)
a = Fraction(總布量, 50)

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 9675051/12500, Actual: 96801/125"""
