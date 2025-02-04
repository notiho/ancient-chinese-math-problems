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
Divide by 50 chi (1 bolt of cloth) to get the number of bolts.

Answer: *a* bolts.
"""

from fractions import Fraction

# Define the number of soldiers
兵 = 3148

# Define the cloth given to each soldier: 1丈2尺3寸
# 1丈 = 10尺, 1尺 = 10寸
布每人 = 1 * 10 + 2 + Fraction(3, 10)  # Convert to 尺

# Total cloth in 尺
總布 = 兵 * 布每人

# Convert to bolts of cloth: 1端 = 50尺
布每端 = 50
a = Fraction(總布, 布每端)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9675051/12500, Actual: 96801/125"""
