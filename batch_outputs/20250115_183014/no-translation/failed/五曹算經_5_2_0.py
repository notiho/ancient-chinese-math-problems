"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a銖 b 絫 c黍 奇 d銖 e黍 。
"""

"""

"""


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

# 戶數
戶數 = 738

# 以七百三十八户除之即得
每戶銖 = Fraction(總銖, 戶數)

# 每銖二十四黍
每銖黍 = 24

# 計算每戶得銖與黍
a = 每戶銖.numerator // 每戶銖.denominator  # 得整銖數
剩餘銖 = 每戶銖 - a  # 剩餘銖部分
b = 剩餘銖.numerator * 每銖黍 // 剩餘銖.denominator  # 得整黍數

# 每黍進一步分解
c = 剩餘銖.numerator * 每銖黍 % 剩餘銖.denominator  # 剩餘黍部分
d = 剩餘銖

"""

"""


"""
Variable 'b' has wrong value. Expected: 2, Actual: 5
Variable 'c' has wrong value. Expected: 1, Actual: 9
Variable 'd' has wrong value. Expected: 1, Actual: 26/123
Missing variable in output: 'e'"""
