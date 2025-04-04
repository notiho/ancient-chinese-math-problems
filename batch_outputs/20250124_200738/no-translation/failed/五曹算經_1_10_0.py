"""
今有田桑生中央從隅至桑一百四十七步。問：為田㡬何？
術曰：列一百四十七步以二乘之得二百九十四步以五乘之得一千四百七十步以七除之得二百一十步自相乘得四萬四千一百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 中央從隅至桑一百四十七步
中央步 = 147

# 列一百四十七步以二乘之
步二倍 = 中央步 * 2

# 得二百九十四步以五乘之
步五倍 = 步二倍 * 5

# 得一千四百七十步以七除之
步七除 = Fraction(步五倍, 7)

# 得二百一十步自相乘
積步 = 步七除 * 步七除

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 百畝為一頃
頃 = 畝數 // 100
奇步 = 畝數 % 100

a = int(頃)
b = 奇步
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 1
Variable 'b' has wrong value. Expected: 180, Actual: 335/4"""
