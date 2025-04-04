"""
今有田桑生中央從隅至桑一百四十七步。問：為田㡬何？
術曰：列一百四十七步以二乘之得二百九十四步以五乘之得一千四百七十步以七除之得二百一十步自相乘得四萬四千一百步以畝法除之即得。
答曰： a(=183/100)頃 奇 b(=180)步 。
"""

#----- content starts here -----
"""
Suppose there is a square field with a mulberry tree in the center. The distance from a corner to the mulberry tree is 147 bu.
Question: how large is the field?

The procedure says: Place 147 bu and multiply it by 2, obtaining 294 bu. Multiply it by 5, obtaining 1470 bu. Divide it by 7, obtaining 210 bu. Square this, obtaining 44100 bu. Divide it by the mu-divisor to obtain the result.

Answer: *a*(=183/100) qing and *b*(=180) bu.
"""

from fractions import Fraction

# 中央從隅至桑一百四十七步
中央至隅 = 147

# 列一百四十七步以二乘之得二百九十四步
步_二倍 = 2 * 中央至隅

# 以五乘之得一千四百七十步
步_五倍 = 5 * 步_二倍

# 以七除之得二百一十步
田邊長 = Fraction(步_五倍, 7)

# 自相乘得四萬四千一百步
田積步 = 田邊長 * 田邊長

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(田積步, 畝法)

# 百畝為一頃
頃數 = 畝數 // 100
奇步 = 畝數 % 100

a = Fraction(頃數, 1) + Fraction(奇步, 100)  # 183/100
b = 奇步  # 180#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 147/80
Variable 'b' has wrong value. Expected: 180, Actual: 335/4"""
