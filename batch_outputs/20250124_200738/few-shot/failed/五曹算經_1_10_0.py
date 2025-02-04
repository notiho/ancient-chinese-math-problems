"""
今有田桑生中央從隅至桑一百四十七步。問：為田㡬何？
術曰：列一百四十七步以二乘之得二百九十四步以五乘之得一千四百七十步以七除之得二百一十步自相乘得四萬四千一百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a square field with a mulberry tree at the center, and the distance from the corner to the mulberry tree is 147 bu.
Question: how large is the field?

The procedure says: Take 147 bu and multiply it by 2, obtaining 294 bu. Multiply this by 5, obtaining 1470 bu. Divide this by 7, obtaining 210 bu. Square this, obtaining 44100 bu. Divide this by the mu-divisor (240), obtaining the result.

Answer: *a* qing and *b* bu.
"""

from fractions import Fraction

# 中央從隅至桑一百四十七步
隅至桑 = 147

# 列一百四十七步以二乘之得二百九十四步
步_二倍 = 隅至桑 * 2

# 以五乘之得一千四百七十步
步_五倍 = 步_二倍 * 5

# 以七除之得二百一十步
田邊長 = Fraction(步_五倍, 7)

# 自相乘得四萬四千一百步
田積步 = 田邊長 * 田邊長

# 畝法
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(田積步, 畝法)

# 百畝為一頃
頃 = 畝數 // 100
剩餘步 = 畝數 % 100

a = int(頃)
b = 剩餘步#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 1
Variable 'b' has wrong value. Expected: 180, Actual: 335/4"""
