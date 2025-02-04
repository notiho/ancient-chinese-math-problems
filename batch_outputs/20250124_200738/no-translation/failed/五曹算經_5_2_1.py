"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a銖 奇 b銖 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 絲二十七斤五两
斤 = 27
兩 = 5

# 每斤十六两
每斤兩 = 16

# 列絲二十七斤，以十六两乘之、納五两，得四百三十七两
總兩 = 斤 * 每斤兩 + 兩

# 每两二十四銖
每兩銖 = 24

# 又以二十四銖乘之，得一萬四百八十八銖
總銖 = 總兩 * 每兩銖

# 七百三十八户
戶數 = 738

# 以七百三十八户除之即得
每戶銖 = Fraction(總銖, 戶數)

# 答曰：a銖 奇 b銖
a = 每戶銖.numerator // 每戶銖.denominator  # 整銖
b = 每戶銖 - a  # 餘銖
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 1421/100, Actual: 14
Variable 'b' has wrong value. Expected: 51/50, Actual: 26/123"""
