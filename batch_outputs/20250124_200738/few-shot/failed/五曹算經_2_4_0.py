"""
今有兵三千一百四十八人，人給布一丈二尺三寸。問：計㡬何？
術曰：列兵三千一百四十八人，以布一十二尺三寸乘之，得三萬八千七百二十尺四寸，以五十尺除之即得。
答曰： a端 。
"""

#----- content starts here -----
"""
Suppose there are 3,148 soldiers, and each soldier is given 1 zhang, 2 chi, and 3 cun of cloth.
Question: how much cloth is needed in total?

The procedure says: Place the 3,148 soldiers, and multiply by the cloth amount of 1 zhang, 2 chi, and 3 cun.
Convert the total to chi, obtaining 38,720 chi and 4 cun.
Divide by 50 chi (1 bolt of cloth) to get the number of bolts.

Answer: *a* bolts.
"""

# 兵三千一百四十八人
兵 = 3148

# 每人給布一丈二尺三寸
丈 = 10  # 1 丈 = 10 尺
尺 = 1   # 1 尺 = 1 尺
寸 = Fraction(1, 10)  # 1 寸 = 1/10 尺

每人布 = 丈 + 2 * 尺 + 3 * 寸

# 以布一十二尺三寸乘之
總布 = 兵 * 每人布

# 以五十尺除之即得
布一端 = 50  # 1 端 = 50 尺
a = Fraction(總布, 布一端)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9675051/12500, Actual: 96801/125"""
