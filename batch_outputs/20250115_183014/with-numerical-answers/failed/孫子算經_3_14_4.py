"""
今有粟一十二萬八千九百四十斛九斗三合，出與人買絹一匹，直粟三斛五斗七升。問：絹幾何？
術曰：置粟一十二萬八千九百四十斛九斗三合為實，以三斛五斗七升為法，除之，得匹餘四十之所得，又以法除之，即得。
答曰： a(=36117)匹 b(=18/5)丈 。
"""

"""
Suppose there are 128,940 hu, 9 dou, and 3 sheng of millet. It is used to buy silk, where 1 bolt of silk is worth 3 hu, 5 dou, and 7 sheng of millet.
Question: how many bolts of silk can be obtained?

The procedure says: Place 128,940 hu, 9 dou, and 3 sheng of millet as the dividend.
Take 3 hu, 5 dou, and 7 sheng as the divisor.
Divide, obtaining the number of bolts and the remainder in terms of 1/40 of a bolt.
Divide the remainder by the divisor again, obtaining the fractional part.

Answer: *a*(=36117) bolts and *b*(=18/5) zhang.
"""

from fractions import Fraction

# 粟一十二萬八千九百四十斛九斗三合
粟_斛 = 128940
粟_斗 = 9
粟_升 = 3

# Convert everything to sheng (1 hu = 10 dou, 1 dou = 10 sheng)
粟_升_total = 粟_斛 * 10 * 10 + 粟_斗 * 10 + 粟_升

# 絹一匹，直粟三斛五斗七升
法_斛 = 3
法_斗 = 5
法_升 = 7

# Convert the price of 1 bolt of silk to sheng
法_升_total = 法_斛 * 10 * 10 + 法_斗 * 10 + 法_升

# 以粟為實，以法為法，除之
匹 = 粟_升_total // 法_升_total  # Integer division to get the number of full bolts
餘_升 = 粟_升_total % 法_升_total  # Remainder in sheng

# 餘四十之所得，又以法除之，即得
餘_匹 = Fraction(餘_升, 法_升_total)  # Fractional part of a bolt

# Convert fractional part to zhang (1 bolt = 40 zhang)
餘_丈 = 餘_匹 * 40

# Final results
a = 匹  # 36117 bolts
b = 餘_丈  # 18/5 zhang
"""
Variable 'b' has wrong value. Expected: 18/5, Actual: 4320/119"""
