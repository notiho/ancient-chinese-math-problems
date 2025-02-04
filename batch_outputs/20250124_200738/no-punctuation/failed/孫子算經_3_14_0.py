"""
今有粟一十二萬八千九百四十斛九斗三合出與人買絹一匹直粟三斛五斗七升問絹幾何
術曰置粟一十二萬八千九百四十斛九斗三合為實以三斛五斗七升為法除之得匹餘四十之所得又以法除之即得
答曰 a匹 
"""

#----- content starts here -----
"""
Suppose there are 128,940 hu, 9 dou, and 3 sheng of millet. It is used to buy silk, where each bolt of silk costs 3 hu, 5 dou, and 7 sheng of millet.
Question: how many bolts of silk can be obtained?

The procedure says: Place 128,940 hu, 9 dou, and 3 sheng of millet as the dividend.
Take 3 hu, 5 dou, and 7 sheng as the divisor.
Divide the dividend by the divisor to obtain the number of bolts, with a remainder in terms of 1/40 of the divisor.
Divide the remainder by the divisor again to obtain the fractional part.

Answer: *a* bolts of silk.
"""

from fractions import Fraction

# 粟一十二萬八千九百四十斛九斗三合
粟_斛 = 128940
粟_斗 = 9
粟_升 = 3

# Convert everything to sheng (1 hu = 10 dou, 1 dou = 10 sheng)
粟_總升 = (粟_斛 * 10 * 10) + (粟_斗 * 10) + 粟_升

# 每匹絹直粟三斛五斗七升
法_斛 = 3
法_斗 = 5
法_升 = 7

# Convert the cost of one bolt of silk to sheng
法_總升 = (法_斛 * 10 * 10) + (法_斗 * 10) + 法_升

# Divide the total millet by the cost of one bolt of silk
匹數 = 粟_總升 // 法_總升  # Integer part (number of full bolts)
餘升 = 粟_總升 % 法_總升  # Remainder in sheng

# Convert the remainder into fractional bolts
餘匹 = Fraction(餘升, 法_總升)

# Total bolts of silk
a = 匹數 + 餘匹#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 361179/10, Actual: 4298031/119"""
