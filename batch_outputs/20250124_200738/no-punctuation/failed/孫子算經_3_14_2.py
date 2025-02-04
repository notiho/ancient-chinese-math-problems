"""
今有粟一十二萬八千九百四十斛九斗三合出與人買絹一匹直粟三斛五斗七升問絹幾何
術曰置粟一十二萬八千九百四十斛九斗三合為實以三斛五斗七升為法除之得匹餘四十之所得又以法除之即得
答曰 a匹 
"""

#----- content starts here -----
"""
Suppose there are 128,940 hu, 9 dou, and 3 sheng of millet. It is used to buy silk, where 1 bolt of silk costs 3 hu, 5 dou, and 7 sheng of millet.
Question: how many bolts of silk can be obtained?

The procedure says: Place the millet, 128,940 hu, 9 dou, and 3 sheng, as the dividend.
Use 3 hu, 5 dou, and 7 sheng as the divisor.
Divide the dividend by the divisor to get the number of bolts and the remainder.
Take the remainder and divide it by the divisor again to get the fractional part.

Answer: *a* bolts.
"""

from fractions import Fraction

# Convert all units to sheng for calculation
# 1 hu = 10 dou, 1 dou = 10 sheng
粟 = (128940 * 10 * 10) + (9 * 10) + 3  # Total millet in sheng

# Convert the price of 1 bolt of silk to sheng
法 = (3 * 10 * 10) + (5 * 10) + 7  # Price of 1 bolt of silk in sheng

# Divide millet by the price of 1 bolt of silk
匹 = 粟 // 法  # Integer part (number of full bolts)
餘 = 粟 % 法  # Remainder in sheng

# Convert the remainder into fractional bolts
餘匹 = Fraction(餘, 法)

# Total bolts of silk
a = 匹 + 餘匹#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 361179/10, Actual: 4298031/119"""
