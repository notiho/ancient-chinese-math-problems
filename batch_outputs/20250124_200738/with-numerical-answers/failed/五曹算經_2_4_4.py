"""
今有兵三千一百四十八人，人給布一丈二尺三寸。問：計㡬何？
術曰：列兵三千一百四十八人，以布一十二尺三寸乘之，得三萬八千七百二十尺四寸，以五十尺除之即得。
答曰： a(=9675051/12500)端 。
"""

#----- content starts here -----
"""
Suppose there are 3148 soldiers. Each soldier is given 1 zhang, 2 chi, and 3 cun of cloth.
Question: how much cloth is needed in total?

The procedure says: Place the 3148 soldiers in a line. Multiply by the cloth length of 1 zhang, 2 chi, and 3 cun, obtaining 38720 chi and 4 cun. Divide by 50 chi to get the total number of bolts.

Answer: *a*(=9675051/12500) bolts.
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
bolt_length = 50  # 1 bolt = 50 尺
a = Fraction(總布_尺, bolt_length)  # 9675051/12500 bolts#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9675051/12500, Actual: 96801/125"""
