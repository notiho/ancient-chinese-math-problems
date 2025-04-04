"""
今有粟一十二萬八千九百四十斛九斗三合，出與人買絹一匹，直粟三斛五斗七升。問：絹幾何？
術曰：置粟一十二萬八千九百四十斛九斗三合為實，以三斛五斗七升為法，除之，得匹餘四十之所得，又以法除之，即得。
答曰： a匹 。
"""

"""
Suppose there are 128,940 hu, 9 dou, and 3 sheng of millet. It is used to buy silk, where 1 bolt of silk costs 3 hu, 5 dou, and 7 sheng of millet.
Question: how many bolts of silk can be obtained?

The procedure says: Place 128,940 hu, 9 dou, and 3 sheng of millet as the dividend.
Use 3 hu, 5 dou, and 7 sheng as the divisor.
Divide the dividend by the divisor, obtaining the number of bolts and the remainder.
Then divide the remainder by the divisor again to obtain the result.

Answer: *a* bolts.
"""

from fractions import Fraction

# 粟一十二萬八千九百四十斛九斗三合
粟_斛 = 128940
粟_斗 = 9
粟_升 = 3

# Convert everything to sheng (1 hu = 10 dou, 1 dou = 10 sheng)
粟_升_total = 粟_斛 * 10 * 10 + 粟_斗 * 10 + 粟_升

# 三斛五斗七升
法_斛 = 3
法_斗 = 5
法_升 = 7

# Convert everything to sheng (1 hu = 10 dou, 1 dou = 10 sheng)
法_升_total = 法_斛 * 10 * 10 + 法_斗 * 10 + 法_升

# Divide the total millet by the cost of one bolt of silk
匹 = 粟_升_total // 法_升_total  # Integer division to get the number of bolts
餘_升 = 粟_升_total % 法_升_total  # Remainder in sheng

# If there's a remainder, calculate the fractional part
餘匹 = Fraction(餘_升, 法_升_total)

# Total bolts of silk (including fractional part)
a = 匹 + 餘匹
"""
Variable 'a' has wrong value. Expected: 361179/10, Actual: 4298031/119"""
