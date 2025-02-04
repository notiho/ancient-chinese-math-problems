"""
今有兵三千一百四十八人，人給布一丈二尺三寸。問：計㡬何？
術曰：列兵三千一百四十八人，以布一十二尺三寸乘之，得三萬八千七百二十尺四寸，以五十尺除之即得。
答曰： a(=9675051/12500)端 。
"""

#----- content starts here -----
"""
Suppose there are 3148 soldiers, and each soldier is given 1 zhang, 2 chi, and 3 cun of cloth.
Question: how much cloth is needed in total?

The procedure says: Place the 3148 soldiers in a line, and multiply by the cloth length of 1 zhang, 2 chi, and 3 cun.
Convert the total into chi (1 zhang = 10 chi, 1 chi = 10 cun).
Divide the result by 50 chi (1 bolt of cloth = 50 chi), obtaining the number of bolts.

Answer: *a*(=9675051/12500) bolts.
"""

# 兵三千一百四十八人
兵 = 3148

# 布一丈二尺三寸
布 = 1 * 10 + 2 + Fraction(3, 10)  # Convert to chi (1丈 = 10尺, 1尺 = 10寸)

# 以布乘兵
總布 = 布 * 兵  # Total cloth in chi

# 以五十尺除之即得
每端 = 50  # 1 bolt = 50 chi
a = Fraction(總布, 每端)  # Result in bolts of cloth#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9675051/12500, Actual: 96801/125"""
