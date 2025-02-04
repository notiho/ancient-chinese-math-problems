"""
今有兵三千一百四十八人，人給布一丈二尺三寸。問：計㡬何？
術曰：列兵三千一百四十八人，以布一十二尺三寸乘之，得三萬八千七百二十尺四寸，以五十尺除之即得。
答曰： a端 。
"""

#----- content starts here -----
"""
Suppose there are 3,148 soldiers, and each soldier is given 1 zhang, 2 chi, and 3 cun of cloth.
Question: how much cloth in total is required, expressed in duan?

The procedure says: Place the number of soldiers, 3,148, and multiply it by the cloth length, 12 chi and 3 cun.
This gives the total length in chi and cun. Convert the total into chi and divide by 50 chi per duan to get the result.

Answer: *a* duan.
"""

from fractions import Fraction

# Number of soldiers
兵 = 3148

# Cloth per soldier: 1 zhang, 2 chi, 3 cun
# 1 zhang = 10 chi, 1 chi = 10 cun
布每人 = 10 + 2 + Fraction(3, 10)  # Convert to chi

# Total cloth in chi
總布 = 兵 * 布每人

# 1 duan = 50 chi
每端 = 50

# Total duan
a = Fraction(總布, 每端)

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9675051/12500, Actual: 96801/125"""
