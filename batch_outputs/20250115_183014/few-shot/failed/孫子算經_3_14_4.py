"""
今有粟一十二萬八千九百四十斛九斗三合，出與人買絹一匹，直粟三斛五斗七升。問：絹幾何？
術曰：置粟一十二萬八千九百四十斛九斗三合為實，以三斛五斗七升為法，除之，得匹餘四十之所得，又以法除之，即得。
答曰： a匹 b丈 。
"""

"""
Suppose there are 128,940 hu, 9 dou, and 3 sheng of millet. It is used to buy silk, where one bolt of silk costs 3 hu, 5 dou, and 7 sheng of millet.
Question: how many bolts of silk can be obtained?

The procedure says: Place 128,940 hu, 9 dou, and 3 sheng of millet as the dividend.
Take 3 hu, 5 dou, and 7 sheng as the divisor.
Divide them, obtaining the number of bolts and the remainder.
Then divide the remainder by the divisor to obtain the fractional part.

Answer: *a* bolts and *b* zhang.
"""

from fractions import Fraction

# 粟一十二萬八千九百四十斛九斗三合
粟_斛 = 128940
粟_斗 = 9
粟_升 = 3

# Convert all to 升 (1 斛 = 10 斗, 1 斗 = 10 升)
粟_升_total = 粟_斛 * 100 + 粟_斗 * 10 + 粟_升

# 三斛五斗七升
法_斛 = 3
法_斗 = 5
法_升 = 7

# Convert all to 升 (1 斛 = 10 斗, 1 斗 = 10 升)
法_升_total = 法_斛 * 100 + 法_斗 * 10 + 法_升

# 以粟為實，以法為法，除之，得匹餘
匹 = 粟_升_total // 法_升_total
餘 = 粟_升_total % 法_升_total

# 餘以法除之，即得
b = Fraction(餘, 法_升_total)

a = 匹  # Number of full bolts
b = b * 10  # Convert fractional part to zhang (1 bolt = 10 zhang)
"""
Variable 'b' has wrong value. Expected: 18/5, Actual: 1080/119"""
