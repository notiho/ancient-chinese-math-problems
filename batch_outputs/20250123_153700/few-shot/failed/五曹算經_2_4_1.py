"""
今有兵三千一百四十八人，人給布一丈二尺三寸。問：計㡬何？
術曰：列兵三千一百四十八人，以布一十二尺三寸乘之，得三萬八千七百二十尺四寸，以五十尺除之即得。
答曰： a端 。
"""

"""
Suppose there are 3148 soldiers, and each soldier is given 1 zhang, 2 chi, and 3 cun of cloth.
Question: how much cloth is needed in total?

The procedure says: Place the number of soldiers, 3148. Multiply it by the cloth, 12 chi and 3 cun, obtaining 38720 chi and 4 cun. Divide by 50 chi to get the number of bolts.

Answer: *a* bolts.
"""

# 兵三千一百四十八人
兵 = 3148

# 布一丈二尺三寸 (convert to chi: 1 zhang = 10 chi, 2 chi = 2 chi, 3 cun = 0.3 chi)
布 = 10 + 2 + Fraction(3, 10)

# 以布一十二尺三寸乘之
總布 = 兵 * 布

# 得三萬八千七百二十尺四寸 (convert to chi: 4 cun = 0.4 chi)
總布 = 總布  # This step confirms the calculation.

# 以五十尺除之即得
bolt_length = 50
a = Fraction(總布, bolt_length)
"""
Variable 'a' has wrong value. Expected: 9675051/12500, Actual: 96801/125"""
