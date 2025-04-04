"""
今有粟一十二萬八千九百四十斛九斗三合，出與人買絹一匹，直粟三斛五斗七升。問：絹幾何？
術曰：置粟一十二萬八千九百四十斛九斗三合為實，以三斛五斗七升為法，除之，得匹餘四十之所得，又以法除之，即得。
答曰： a匹 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 粟一十二萬八千九百四十斛九斗三合
粟 = 128940 + Fraction(9, 10) + Fraction(3, 100)

# 絹一匹，直粟三斛五斗七升
法 = 3 + Fraction(5, 10) + Fraction(7, 100)

# 置粟為實，以法除之，得匹餘四十之所得
匹 = 粟 // 法
餘 = 粟 % 法

# 又以法除之，即得
餘匹 = Fraction(餘, 法)

# 總匹數
a = 匹 + 餘匹
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 361179/10, Actual: 4298031/119"""
