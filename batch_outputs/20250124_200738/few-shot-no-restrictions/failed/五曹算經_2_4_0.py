"""
今有兵三千一百四十八人，人給布一丈二尺三寸。問：計㡬何？
術曰：列兵三千一百四十八人，以布一十二尺三寸乘之，得三萬八千七百二十尺四寸，以五十尺除之即得。
答曰： a端 。
"""

#----- content starts here -----
"""
Suppose there are 3,148 soldiers, and each soldier is given 1 zhang, 2 chi, and 3 cun of cloth.
Question: how much cloth is required in total?

The procedure says: Place the 3,148 soldiers, and multiply it by the cloth amount of 12 chi and 3 cun.
This gives 38,720 chi and 4 cun.
Divide this by 50 chi to convert to bolts of cloth.

Answer: *a* bolts.
"""

from fractions import Fraction

# 兵三千一百四十八人
兵 = 3148

# 每人給布一丈二尺三寸
布每人 = 1 * 10 + 2 + Fraction(3, 10)  # 1 zhang = 10 chi, 2 chi, 3 cun (1 chi = 10 cun)

# 總布量
總布量 = 兵 * 布每人  # in chi

# 每端布五十尺
每端布 = 50  # in chi

# 計算端數
a = Fraction(總布量, 每端布)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9675051/12500, Actual: 96801/125"""
