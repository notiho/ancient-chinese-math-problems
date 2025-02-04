"""
今有兵三千一百四十八人，人給布一丈二尺三寸。問：計㡬何？
術曰：列兵三千一百四十八人，以布一十二尺三寸乘之，得三萬八千七百二十尺四寸，以五十尺除之即得。
答曰： a端 。
"""

#----- content starts here -----
"""
Suppose there are 3148 soldiers, and each soldier is given 1 zhang, 2 chi, and 3 cun of cloth.
Question: how much cloth is needed in total?

The procedure says: Place the 3148 soldiers, and multiply by the cloth amount of 1 zhang, 2 chi, and 3 cun. 
Convert the total to chi, obtaining 38720 chi and 4 cun. 
Divide by 50 chi (1 bolt of cloth) to determine the number of bolts.

Answer: *a* bolts.
"""

from fractions import Fraction

# Constants for unit conversion
ZHANG_TO_CHI = 10  # 1 zhang = 10 chi
CHI_TO_CUN = 10    # 1 chi = 10 cun
BOLT_LENGTH = 50   # 1 bolt = 50 chi

# Number of soldiers
兵 = 3148

# Cloth per soldier: 1 zhang, 2 chi, 3 cun
布_per_soldier = ZHANG_TO_CHI + 2 + Fraction(3, CHI_TO_CUN)  # Convert to chi

# Total cloth in chi
總布 = 兵 * 布_per_soldier

# Convert total cloth to bolts
a = Fraction(總布, BOLT_LENGTH)

# Output
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9675051/12500, Actual: 96801/125"""
