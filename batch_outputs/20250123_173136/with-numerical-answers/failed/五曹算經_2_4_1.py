"""
今有兵三千一百四十八人，人給布一丈二尺三寸。問：計㡬何？
術曰：列兵三千一百四十八人，以布一十二尺三寸乘之，得三萬八千七百二十尺四寸，以五十尺除之即得。
答曰： a(=9675051/12500)端 。
"""

"""
Suppose there are 3148 soldiers, and each soldier is given 1 zhang, 2 chi, and 3 cun of cloth.
Question: how much cloth is needed in total?

The procedure says: Place the 3148 soldiers, and multiply by 1 zhang, 2 chi, and 3 cun of cloth.
This gives 38720 chi and 4 cun.
Divide by 50 chi to convert to duan.

Answer: *a*(=9675051/12500) duan.
"""

from fractions import Fraction

# 兵三千一百四十八人
兵 = 3148

# 每人給布一丈二尺三寸
布_丈 = 1
布_尺 = 2
布_寸 = 3

# 1 丈 = 10 尺, 1 尺 = 10 寸
布_總尺 = 布_丈 * 10 + 布_尺 + 布_寸 / 10

# 以布一十二尺三寸乘之
總布_尺 = 兵 * 布_總尺

# 以五十尺除之即得
a = Fraction(總布_尺, 50) # 9675051/12500 duan
"""
Code error: both arguments should be Rational instances"""
