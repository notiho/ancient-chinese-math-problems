"""
今有粟一十二萬八千九百四十斛九斗三合出與人買絹一匹直粟三斛五斗七升問絹幾何
術曰置粟一十二萬八千九百四十斛九斗三合為實以三斛五斗七升為法除之得匹餘四十之所得又以法除之即得
答曰 a匹 
"""

#----- content starts here -----
"""
Suppose there are 128,940 hu, 9 dou, and 3 sheng of millet. It is used to buy silk, where 1 bolt of silk is worth 3 hu, 5 dou, and 7 sheng of millet.
Question: how many bolts of silk can be obtained?

The procedure says: Place 128,940 hu, 9 dou, and 3 sheng of millet as the dividend.
Take 3 hu, 5 dou, and 7 sheng as the divisor.
Divide the dividend by the divisor to obtain the number of bolts and the remainder.
Take the remainder and divide it again by the divisor to obtain the fractional part.

Answer: *a* bolts of silk.
"""

# Convert all units to sheng for consistency
# 1 hu = 10 dou, 1 dou = 10 sheng
粟 = (128940 * 10 * 10) + (9 * 10) + 3  # Convert 128,940 hu, 9 dou, 3 sheng to sheng

# Convert the price of 1 bolt of silk to sheng
法 = (3 * 10 * 10) + (5 * 10) + 7  # Convert 3 hu, 5 dou, 7 sheng to sheng

# Divide to find the number of bolts and the remainder
匹 = 粟 // 法  # Integer division to find the number of bolts
餘 = 粟 % 法  # Remainder in sheng

# Convert the remainder to fractional bolts
fractional_part = Fraction(餘, 法)

# Total bolts of silk
a = 匹 + fractional_part#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 361179/10, Actual: 4298031/119"""
