"""
今有方田桑生中央，從角至桑，一百四十七步。問：為田幾何？
術曰：置角至桑一百四十七步，倍之，得二百九十四步，以五乘之，得一千四百七十步，以七除之，得二百一十步，自相乘，得四萬四千一百步，以二百四十步除之，即得。
答曰： a頃 ，奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a square field with a mulberry tree growing at the center.
From a corner of the field to the mulberry tree, it is 147 bu.
Question: how large is the field?

The procedure says: Place the distance from the corner to the mulberry tree as 147 bu.
Double it, obtaining 294 bu.
Multiply it by 5, obtaining 1470 bu.
Divide it by 7, obtaining 210 bu.
Square this result, obtaining 44100 bu.
Divide it by 240 bu, obtaining the result.

Answer: *a* qing, with a remainder of *b* bu.
"""

from fractions import Fraction

# 置角至桑一百四十七步
角至桑 = 147

# 倍之，得二百九十四步
倍步 = 2 * 角至桑

# 以五乘之，得一千四百七十步
乘五步 = 5 * 倍步

# 以七除之，得二百一十步
正方邊長 = Fraction(乘五步, 7)

# 自相乘，得四萬四千一百步
田積步 = 正方邊長 * 正方邊長

# 以二百四十步除之，即得
畝數 = Fraction(田積步, 240)

# 100 畝為 1 頃
頃數 = 畝數 // 100
奇步 = 畝數 % 100

a = int(頃數)
b = 奇步
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 1
Variable 'b' has wrong value. Expected: 180, Actual: 335/4"""
