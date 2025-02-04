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
Multiply the cloth of 1 zhang, 2 chi, and 3 cun by the number of soldiers, obtaining the total in chi and cun.
Divide it by 50 chi (1 bolt of cloth), and the result is the number of bolts.

Answer: *a* bolts.
"""

# 兵三千一百四十八人
兵 = 3148

# 布一丈二尺三寸 (convert to chi: 1 zhang = 10 chi, 1 chi = 10 cun)
布 = 10 + 2 + Fraction(3, 10)

# 以布乘兵，得總布尺數
總布尺數 = 布 * 兵

# 以五十尺除之，即得端數
a = Fraction(總布尺數, 50)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9675051/12500, Actual: 96801/125"""
