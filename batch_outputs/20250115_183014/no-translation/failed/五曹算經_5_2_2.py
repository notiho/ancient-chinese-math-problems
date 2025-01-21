"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a銖 b 絫 c黍 奇 d銖 e黍 。
"""

"""

"""


from fractions import Fraction

# 絲二十七斤五两
絲斤 = 27
絲兩 = 5

# 每斤十六两
每斤兩 = 16

# 列絲二十七斤，以十六两乘之、納五两，得四百三十七两
總兩 = (絲斤 * 每斤兩) + 絲兩

# 每两二十四銖
每兩銖 = 24

# 又以二十四銖乘之，得一萬四百八十八銖
總銖 = 總兩 * 每兩銖

# 七百三十八户
戶數 = 738

# 以七百三十八户除之即得
每戶銖 = Fraction(總銖, 戶數)

# 每銖二十絫
每銖絫 = 20

# 每絫二十四黍
每絫黍 = 24

# 計算戶得
a = 每戶銖.numerator // 每戶銖.denominator  # 銖
剩餘銖 = 每戶銖 - a

b = (剩餘銖 * 每銖絫).numerator // (剩餘銖 * 每銖絫).denominator  # 絫
剩餘絫 = (剩餘銖 * 每銖絫) - b

c = (剩餘絫 * 每絫黍).numerator // (剩餘絫 * 每絫黍).denominator  # 黍
剩餘黍 = (剩餘絫 * 每絫黍) - c

d = 剩餘黍.numerator // 剩餘黍.denominator  # 奇銖
e = 剩餘黍 - d  # 奇黍

# 答案
a銖 = a
b絫 = b
c黍 = c
d奇銖 = d
e奇黍 = e


"""

"""


"""
Variable 'b' has wrong value. Expected: 2, Actual: 4
Variable 'c' has wrong value. Expected: 1, Actual: 5
Variable 'd' has wrong value. Expected: 1, Actual: 0
Variable 'e' has wrong value. Expected: 2, Actual: 19/41"""
