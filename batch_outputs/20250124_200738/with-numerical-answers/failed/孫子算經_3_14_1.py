"""
今有粟一十二萬八千九百四十斛九斗三合，出與人買絹一匹，直粟三斛五斗七升。問：絹幾何？
術曰：置粟一十二萬八千九百四十斛九斗三合為實，以三斛五斗七升為法，除之，得匹餘四十之所得，又以法除之，即得。
答曰： a(=361179/10)匹 。
"""

#----- content starts here -----
"""
Suppose there are 128,940 hu, 9 dou, and 3 sheng of millet. It is used to buy silk, where one bolt of silk is worth 3 hu, 5 dou, and 7 sheng of millet.
Question: how many bolts of silk can be obtained?

The procedure says: Place 128,940 hu, 9 dou, and 3 sheng of millet as the dividend.
Take 3 hu, 5 dou, and 7 sheng as the divisor.
Divide, obtaining the number of bolts and the remainder.
Then divide the remainder by the divisor again to obtain the result.

Answer: *a*(=361179/10) bolts of silk.
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

# Convert divisor to 升
法_升_total = 法_斛 * 100 + 法_斗 * 10 + 法_升

# Divide to find the number of bolts of silk
a = Fraction(粟_升_total, 法_升_total)  # 361179/10#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 361179/10, Actual: 4298031/119"""
