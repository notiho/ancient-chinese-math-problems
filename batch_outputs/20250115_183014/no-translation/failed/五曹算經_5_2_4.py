"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
術曰：列絲二十七斤，以十六两乘之、納五两，得四百三十七两；又以二十四銖乘之，得一萬四百八十八銖；以七百三十八户除之即得。
答曰： a銖 b 絫 c黍 奇 d銖 e黍 。
"""

"""

"""


from fractions import Fraction

# 絲二十七斤五两
絲_斤 = 27
絲_兩 = 5

# 戶數
戶數 = 738

# 列絲二十七斤，以十六两乘之、納五两，得四百三十七两
絲_總兩 = (絲_斤 * 16) + 絲_兩

# 又以二十四銖乘之，得一萬四百八十八銖
絲_總銖 = 絲_總兩 * 24

# 以七百三十八户除之即得
每戶_銖 = Fraction(絲_總銖, 戶數)

# 銖轉換為絫與黍
銖_每戶 = 每戶_銖.numerator // 每戶_銖.denominator
剩餘_銖 = 每戶_銖 - 銖_每戶

絫_每戶 = 剩餘_銖.numerator // 剩餘_銖.denominator


"""

"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'
Missing variable in output: 'e'"""
