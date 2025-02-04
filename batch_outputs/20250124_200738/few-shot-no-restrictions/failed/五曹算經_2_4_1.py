"""
今有兵三千一百四十八人，人給布一丈二尺三寸。問：計㡬何？
術曰：列兵三千一百四十八人，以布一十二尺三寸乘之，得三萬八千七百二十尺四寸，以五十尺除之即得。
答曰： a端 。
"""

#----- content starts here -----
"""
Suppose there are 3,148 soldiers, and each soldier is given 1 zhang, 2 chi, and 3 cun of cloth.
Question: how much cloth is needed in total, expressed in duan (a unit where 1 duan = 50 chi)?

The procedure says: Place the number of soldiers, 3,148, and multiply it by the amount of cloth per soldier (1 zhang, 2 chi, 3 cun). 
Convert the total to chi, then divide by 50 chi to get the number of duan.

Answer: *a* duan.
"""

from fractions import Fraction

# Constants for unit conversion
ZHANG_TO_CHI = 10  # 1 zhang = 10 chi
CHI_TO_CUN = 10    # 1 chi = 10 cun
DUAN_TO_CHI = 50   # 1 duan = 50 chi

# Number of soldiers
兵 = 3148

# Cloth per soldier: 1 zhang, 2 chi, 3 cun
布每人 = ZHANG_TO_CHI * 1 + 2 + Fraction(3, CHI_TO_CUN)  # Convert to chi

# Total cloth in chi
總布 = 兵 * 布每人

# Convert total cloth to duan
a = Fraction(總布, DUAN_TO_CHI)

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9675051/12500, Actual: 96801/125"""
