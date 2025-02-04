"""
今有兵三千一百四十八人人給布一丈二尺三寸問計㡬何
術曰列兵三千一百四十八人以布一十二尺三寸乘之得三萬八千七百二十尺四寸以五十尺除之即得
答曰 a端 
"""

#----- content starts here -----
"""
Suppose there are 3148 soldiers, and each is given 1 zhang, 2 chi, and 3 cun of cloth.
Question: how much cloth is needed in total?

The procedure says: Place the 3148 soldiers in a line.
Multiply the cloth of 1 zhang, 2 chi, and 3 cun by the number of soldiers, obtaining 38720 chi and 4 cun.
Divide by 50 chi to obtain the number of bolts of cloth.

Answer: *a* bolts.
"""

# 列兵三千一百四十八人
兵 = 3148

# 布一丈二尺三寸
布_丈 = 1
布_尺 = 2
布_寸 = 3

# Convert 布 to 尺 (1 丈 = 10 尺, 1 尺 = 10 寸)
布_總尺 = 布_丈 * 10 + 布_尺 + 布_寸 / 10

# 以布乘兵，得總布尺
總布尺 = 布_總尺 * 兵

# 以五十尺除之
bolt_length = 50  # 每端布長 50 尺
a = Fraction(總布尺, bolt_length)  # 得端數#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
