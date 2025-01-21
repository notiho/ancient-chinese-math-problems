"""
今有粟一十二萬八千九百四十斛九斗三合出與人買絹一匹直粟三斛五斗七升問絹幾何
術曰置粟一十二萬八千九百四十斛九斗三合為實以三斛五斗七升為法除之得匹餘四十之所得又以法除之即得
答曰 a匹 b丈 
"""

"""
Suppose there are 128,940 hu, 9 dou, and 3 sheng of millet. It is used to buy silk, where 1 bolt of silk costs 3 hu, 5 dou, and 7 sheng of millet.
Question: how many bolts of silk can be obtained?

The procedure says: Place the millet, 128,940 hu, 9 dou, and 3 sheng, as the dividend.
Take 3 hu, 5 dou, and 7 sheng as the divisor.
Divide the dividend by the divisor to obtain the number of bolts, with a remainder.
Take the remainder and divide it again by the divisor to obtain the fractional part.

Answer: *a* bolts and *b* tenths of a bolt.
"""

from fractions import Fraction

# 粟一十二萬八千九百四十斛九斗三合
粟 = 128940 * 10 + 9 + Fraction(3, 10)  # Convert to dou (1 hu = 10 dou, 1 dou = 10 sheng)

# 絹一匹直粟三斛五斗七升
匹價值 = 3 * 10 + 5 + Fraction(7, 10)  # Convert to dou

# 以粟為實，以匹價值為法除之
a = int(粟 // 匹價值)  # Number of whole bolts
餘粟 = 粟 % 匹價值  # Remaining millet

# 餘粟再以匹價值除之，得分數部分
b = Fraction(餘粟, 匹價值)  # Fractional part of a bolt
"""
Variable 'b' has wrong value. Expected: 18/5, Actual: 108/119"""
