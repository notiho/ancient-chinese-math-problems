"""
今有粟一十二萬八千九百四十斛九斗三合出與人買絹一匹直粟三斛五斗七升問絹幾何
術曰置粟一十二萬八千九百四十斛九斗三合為實以三斛五斗七升為法除之得匹餘四十之所得又以法除之即得
答曰 a匹 b丈 
"""

"""
Suppose there are 128,940 hu, 9 dou, and 3 sheng of millet. It is used to buy silk, where one bolt of silk costs 3 hu, 5 dou, and 7 sheng of millet.
Question: how many bolts of silk can be obtained?

The procedure says: Place the millet, 128,940 hu, 9 dou, and 3 sheng, as the dividend.
Take 3 hu, 5 dou, and 7 sheng as the divisor.
Divide the dividend by the divisor to obtain the number of bolts and the remainder.
Take the remainder and divide it again by the divisor to obtain the fractional part.

Answer: *a* bolts and *b* zhang.
"""

# 粟一十二萬八千九百四十斛九斗三合
粟 = (128940 * 10 + 9) * 10 + 3  # Convert to sheng (1 hu = 10 dou, 1 dou = 10 sheng)

# 一匹直粟三斛五斗七升
法 = (3 * 10 + 5) * 10 + 7  # Convert to sheng

# 以粟為實，以法除之，得匹
a = 粟 // 法  # Number of full bolts

# 餘四十之所得
餘 = 粟 % 法  # Remaining millet in sheng

# 又以法除之，即得
b = Fraction(餘, 法)  # Fractional part of a bolt

# Convert fractional part to zhang (1 bolt = 10 zhang)
b = b * 10  # Convert to zhang
"""
Variable 'b' has wrong value. Expected: 18/5, Actual: 1080/119"""
