"""
今有粟一十二萬八千九百四十斛九斗三合出與人買絹一匹直粟三斛五斗七升問絹幾何
術曰置粟一十二萬八千九百四十斛九斗三合為實以三斛五斗七升為法除之得匹餘四十之所得又以法除之即得
答曰 a匹 b丈 
"""

"""
Suppose there are 128,940 hu, 9 dou, and 3 sheng of millet. It is used to buy silk, where 1 bolt of silk costs 3 hu, 5 dou, and 7 sheng of millet.
Question: how many bolts of silk can be purchased?

The procedure says: Place 128,940 hu, 9 dou, and 3 sheng of millet as the dividend.
Take 3 hu, 5 dou, and 7 sheng as the divisor.
Divide the dividend by the divisor to obtain the number of bolts, with a remainder.
Take the remainder and divide it again by the divisor to obtain the fractional part.

Answer: *a* bolts and *b* zhang.
"""

# 粟一十二萬八千九百四十斛九斗三合
粟 = 128940  # 斛
粟 += Fraction(9, 10)  # 9斗 = 9/10斛
粟 += Fraction(3, 100)  # 3升 = 3/100斛

# 一匹直粟三斛五斗七升
法 = 3  # 斛
法 += Fraction(5, 10)  # 5斗 = 5/10斛
法 += Fraction(7, 100)  # 7升 = 7/100斛

# 以粟為實，以法為法，除之得匹
匹 = 粟 // 法  # 整數部分為匹數
餘 = 粟 % 法  # 餘數

# 餘四十之所得，又以法除之，即得
丈 = Fraction(餘, 法)  # 餘數轉化為小數部分

a = 匹
b = 丈
"""
Variable 'b' has wrong value. Expected: 18/5, Actual: 108/119"""
