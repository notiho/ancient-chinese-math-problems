"""
今有兵三千一百四十八人，人給布一丈二尺三寸。問：計㡬何？
術曰：列兵三千一百四十八人，以布一十二尺三寸乘之，得三萬八千七百二十尺四寸，以五十尺除之即得。
答曰： a(=9675051/12500)端 。
"""

#----- content starts here -----
"""
Suppose there are 3148 soldiers, and each soldier is given 1 zhang, 2 chi, and 3 cun of cloth.
Question: how much cloth is needed in total?

The procedure says: Place the 3148 soldiers in a line, and multiply by the cloth of 1 zhang, 2 chi, and 3 cun.
Obtain the total in chi and cun. Divide by 50 chi (1 duan = 50 chi), and the result is the total number of duan.

Answer: *a*(=9675051/12500) duan.
"""

# 兵三千一百四十八人
兵 = 3148

# 布一丈二尺三寸
布_丈 = 1
布_尺 = 2
布_寸 = 3

# Convert 布 to 尺 (1 丈 = 10 尺, 1 尺 = 10 寸)
布_總尺 = 布_丈 * 10 + 布_尺 + Fraction(布_寸, 10)

# 以布一十二尺三寸乘之
總布_尺 = 兵 * 布_總尺

# 以五十尺除之即得
每端_尺 = 50
a = Fraction(總布_尺, 每端_尺) # 9675051/12500 duan#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9675051/12500, Actual: 96801/125"""
