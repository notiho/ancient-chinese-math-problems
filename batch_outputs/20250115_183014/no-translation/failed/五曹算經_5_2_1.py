"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a銖 b 絫 c黍 奇 d銖 e黍 。
"""

"""

"""


# 絲二十七斤五两
斤 = 27
兩 = 5

# 每斤十六两
每斤兩 = 16

# 列絲二十七斤，以十六两乘之、納五两，得四百三十七两
總兩 = 斤 * 每斤兩 + 兩

# 每兩二十四銖
每兩銖 = 24

# 又以二十四銖乘之，得一萬四百八十八銖
總銖 = 總兩 * 每兩銖

# 戶數
戶數 = 738

# 以七百三十八户除之即得
每戶銖 = Fraction(總銖, 戶數)

# 每銖二十四絫
每銖絫 = 24

# 每絫六黍
每絫黍 = 6

# 計算戶得
a = 每戶銖.numerator // 每戶銖.denominator  # 銖
剩餘銖 = 每戶銖 - a
b = (剩餘銖 * 每銖絫).numerator // (剩餘銖 * 每銖絫).denominator  # 絫
剩餘絫 = (剩餘銖 * 每銖絫) - b
c = (剩餘絫 * 每絫黍).numerator // (剩餘絫 * 每絫黍).denominator  # 黍
剩餘黍 = (剩餘絫 * 每絫黍) - c
d = 剩餘黍.numerator // 剩餘黍.denominator  # 奇銖
e = (剩餘黍 - d).numerator  # 奇黍


"""

"""


"""
Variable 'b' has wrong value. Expected: 2, Actual: 5
Variable 'c' has wrong value. Expected: 1, Actual: 0
Variable 'd' has wrong value. Expected: 1, Actual: 0
Variable 'e' has wrong value. Expected: 2, Actual: 18"""
