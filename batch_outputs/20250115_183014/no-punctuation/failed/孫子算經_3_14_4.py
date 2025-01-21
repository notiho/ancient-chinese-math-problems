"""
今有粟一十二萬八千九百四十斛九斗三合出與人買絹一匹直粟三斛五斗七升問絹幾何
術曰置粟一十二萬八千九百四十斛九斗三合為實以三斛五斗七升為法除之得匹餘四十之所得又以法除之即得
答曰 a匹 b丈 
"""

"""
Suppose there are 128,940 hu, 9 dou, and 3 sheng of millet. 
It is used to buy silk, where 1 bolt of silk is worth 3 hu, 5 dou, and 7 sheng of millet.
Question: how many bolts of silk can be obtained?

The procedure says: Place 128,940 hu, 9 dou, and 3 sheng of millet as the dividend.
Use 3 hu, 5 dou, and 7 sheng as the divisor.
Divide, obtaining the number of bolts and the remainder.
Take the remainder and divide it again by the divisor, obtaining the fractional part.

Answer: *a* bolts and *b* zhang.
"""

# 粟一十二萬八千九百四十斛九斗三合
粟_斛 = 128940
粟_斗 = 9
粟_升 = 3

# Convert everything to sheng (1 hu = 10 dou, 1 dou = 10 sheng)
粟_升 += 粟_斗 * 10 + 粟_斛 * 100

# 一匹絹直粟三斛五斗七升
法_斛 = 3
法_斗 = 5
法_升 = 7

# Convert everything to sheng (1 hu = 10 dou, 1 dou = 10 sheng)
法_升 += 法_斗 * 10 + 法_斛 * 100

# Divide to find the number of bolts and the remainder
a = 粟_升 // 法_升  # Number of bolts
餘 = 粟_升 % 法_升  # Remainder in sheng

# Convert the remainder into fractional bolts
b = Fraction(餘, 法_升)  # Fractional part of a bolt (in zhang)
"""
Variable 'b' has wrong value. Expected: 18/5, Actual: 108/119"""
