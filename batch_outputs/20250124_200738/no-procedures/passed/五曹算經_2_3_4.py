"""
今有兵三千八百三十七人，人給錢五百五十六文。問：計㡬何？
答曰： a貫 。
"""

#----- content starts here -----
"""
Suppose there are 3837 soldiers, and each soldier is given 556 wen (a unit of currency).
Question: how many guan (strings of coins, where 1 guan = 1000 wen) are needed in total?

Answer: *a* guan.
"""

# 兵三千八百三十七人
兵 = 3837

# 每人給錢五百五十六文
每人錢 = 556

# 總文數
總文數 = 兵 * 每人錢

# 換算成貫 (1貫 = 1000文)
a = Fraction(總文數, 1000)#----- content ends here -----

"""
"""
