"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a銖 b 絫 c黍 奇 d銖 e黍 。
"""

"""

"""


from fractions import Fraction

# 絲二十七斤五两
斤 = 27
兩 = 5

# 列絲二十七斤，以十六两乘之、納五两
總兩 = 斤 * 16 + 兩

# 得四百三十七两
總銖 = 總兩 * 24  # 每兩有24銖

# 又以二十四銖乘之，得一萬四百八十八銖
總銖 = 總兩 * 24

# 七百三十八户
戶數 = 738

# 以七百三十八户除之即得
每戶銖 = Fraction(總銖, 戶數)

# 轉換為銖、絫、黍
銖 = 每戶銖 // 24  # 每絫有24銖
剩餘銖 = 每戶銖 % 24

絫 = 剩餘銖 // 1  # 每絫有1銖
剩餘黍 = 剩餘銖 % 1

黍 = 剩餘黍 * 24  # 每銖有24黍

a = int(銖)
b = int(絫)
c = int(黍)
d = int(剩餘銖)
e = int(剩餘黍)

# 答曰：a銖 b絫 c黍 奇 d銖 e黍。


"""

"""


"""
Variable 'a' has wrong value. Expected: 14, Actual: 0
Variable 'b' has wrong value. Expected: 2, Actual: 14
Variable 'c' has wrong value. Expected: 1, Actual: 5
Variable 'd' has wrong value. Expected: 1, Actual: 14
Variable 'e' has wrong value. Expected: 2, Actual: 0"""
