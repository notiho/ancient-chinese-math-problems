"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a銖 奇 b銖 。
"""

"""

"""


from fractions import Fraction

# 絲二十七斤五两
斤 = 27
兩 = 5

# 以十六两乘之、納五两，得四百三十七两
總兩 = 斤 * 16 + 兩

# 又以二十四銖乘之
總銖 = 總兩 * 24

# 七百三十八户
戶數 = 738

# 以七百三十八户除之即得
每戶銖 = Fraction(總銖, 戶數)

# 答曰：a銖 奇 b銖
a = 每戶銖.numerator // 每戶銖.denominator  # 整數部分
b = 每戶銖 - a  # 餘數部分


"""

"""


"""
Variable 'a' has wrong value. Expected: 1421/100, Actual: 14
Variable 'b' has wrong value. Expected: 51/50, Actual: 26/123"""
