"""
今有粟一十二萬八千九百四十斛九斗三合，出與人買絹一匹，直粟三斛五斗七升。問：絹幾何？
術曰：置粟一十二萬八千九百四十斛九斗三合為實，以三斛五斗七升為法，除之，得匹餘四十之所得，又以法除之，即得。
答曰： a匹 b丈 。
"""

"""

"""


from fractions import Fraction

# 粟一十二萬八千九百四十斛九斗三合
粟_斛 = 128940
粟_斗 = 9
粟_合 = 3

# Convert everything to 合 (1斛 = 10斗, 1斗 = 10升, 1升 = 10合)
粟_合_total = (粟_斛 * 10 * 10) + (粟_斗 * 10) + 粟_合

# 絹一匹，直粟三斛五斗七升
法_斛 = 3
法_斗 = 5
法_升 = 7

# Convert 法 to 合
法_合 = (法_斛 * 10 * 10) + (法_斗 * 10) + (法_升 * 10)

# 置粟為實，以法除之，得匹餘四十之所得
匹 = 粟_合_total // 法_合
餘_合 = 粟_合_total % 法_合

# 又以法除之，即得
餘_匹 = Fraction(餘_合, 法_合)

# Convert 餘_匹 to 丈 (1匹 = 40丈)
餘_丈 = 餘_匹 * 40

# Final result
a = 匹
b = 餘_丈


"""

"""


"""
Variable 'a' has wrong value. Expected: 36117, Actual: 30700
Variable 'b' has wrong value. Expected: 18/5, Actual: 62/7"""
