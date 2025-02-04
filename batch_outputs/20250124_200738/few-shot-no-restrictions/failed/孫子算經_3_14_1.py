"""
今有粟一十二萬八千九百四十斛九斗三合，出與人買絹一匹，直粟三斛五斗七升。問：絹幾何？
術曰：置粟一十二萬八千九百四十斛九斗三合為實，以三斛五斗七升為法，除之，得匹餘四十之所得，又以法除之，即得。
答曰： a匹 。
"""

#----- content starts here -----
"""
Suppose there are 128,940 hu, 9 dou, and 3 sheng of millet. It is used to buy silk, where one bolt of silk costs 3 hu, 5 dou, and 7 sheng of millet.
Question: how many bolts of silk can be obtained?

The procedure says: Place the total millet (128,940 hu, 9 dou, 3 sheng) as the dividend.
Take 3 hu, 5 dou, and 7 sheng as the divisor, and divide.
The result is the number of bolts obtained, with a remainder.
Divide the remainder by the divisor again to determine the fractional part.

Answer: *a* bolts.
"""

from fractions import Fraction

# Convert all units to sheng for uniformity
# 1 hu = 10 dou, 1 dou = 10 sheng
粟 = (128940 * 10 * 10) + (9 * 10) + 3  # Total millet in sheng

# Cost of one bolt of silk in sheng
法 = (3 * 10 * 10) + (5 * 10) + 7  # 3 hu, 5 dou, 7 sheng in sheng

# Perform division to find the number of bolts and the remainder
匹 = 粟 // 法  # Integer part (number of full bolts)
餘 = 粟 % 法  # Remainder in sheng

# Convert the remainder into fractional bolts
餘匹 = Fraction(餘, 法)

# Total bolts of silk
a = 匹 + 餘匹

a  # Output the result as the total number of bolts of silk#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 361179/10, Actual: 4298031/119"""
