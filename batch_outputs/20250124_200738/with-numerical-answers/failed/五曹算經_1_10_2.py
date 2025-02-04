"""
今有田桑生中央從隅至桑一百四十七步。問：為田㡬何？
術曰：列一百四十七步以二乘之得二百九十四步以五乘之得一千四百七十步以七除之得二百一十步自相乘得四萬四千一百步以畝法除之即得。
答曰： a(=183/100)頃 奇 b(=180)步 。
"""

#----- content starts here -----
"""
Suppose there is a square field with a mulberry tree in the center. The distance from a corner to the mulberry tree is 147 bu.
Question: how large is the area of the field?

The procedure says: Take 147 bu, multiply it by 2, obtaining 294 bu. Multiply it by 5, obtaining 1470 bu. Divide it by 7, obtaining 210 bu. Square this value, obtaining 44100 bu². Divide it by the mu-divisor (240 bu² per mu), obtaining the area in mu.

The answer says: *a*(=183/100) qing and *b*(=180) bu.
"""

from fractions import Fraction

# 中央從隅至桑一百四十七步
隅至桑 = 147

# 列一百四十七步以二乘之得二百九十四步
步_二倍 = 2 * 隅至桑

# 以五乘之得一千四百七十步
步_五倍 = 5 * 步_二倍

# 以七除之得二百一十步
田邊長 = Fraction(步_五倍, 7)

# 自相乘得四萬四千一百步
田積步 = 田邊長 * 田邊長

# 以畝法除之即得
畝法 = 240  # 240 bu² per mu
田積畝 = Fraction(田積步, 畝法)

# Convert to qing and remaining bu
畝每頃 = 100  # 100 mu per qing
田積頃 = 田積畝 // 畝每頃
田積餘步 = (田積畝 % 畝每頃) * 畝法

a = Fraction(田積頃) + Fraction(田積畝 % 畝每頃, 畝每頃)  # 183/100 qing
b = int(田積餘步)  # 180 bu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 147/80
Variable 'b' has wrong value. Expected: 180, Actual: 20100"""
