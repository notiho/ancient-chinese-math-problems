"""
今有方田桑生中央，從角至桑，一百四十七步。問：為田幾何？
術曰：置角至桑一百四十七步，倍之，得二百九十四步，以五乘之，得一千四百七十步，以七除之，得二百一十步，自相乘，得四萬四千一百步，以二百四十步除之，即得。
答曰： a(=183/100)頃 ，奇 b(=180)步 。
"""

"""
Suppose there is a square field with a mulberry tree growing in the center. The distance from a corner to the mulberry tree is 147 bu.
Question: how large is the field?

The procedure says: Place the distance from the corner to the mulberry tree, 147 bu, and double it, obtaining 294 bu.
Multiply it by 5, obtaining 1470 bu.
Divide it by 7, obtaining 210 bu.
Square it, obtaining 44100 bu.
Divide it by 240 bu, obtaining the result.

Answer: *a*(=183/100) qing, with a remainder of *b*(=180) bu.
"""

from fractions import Fraction

# 置角至桑一百四十七步
角至桑 = 147

# 倍之，得二百九十四步
倍角至桑 = 2 * 角至桑

# 以五乘之，得一千四百七十步
五乘 = 5 * 倍角至桑

# 以七除之，得二百一十步
田邊長 = Fraction(五乘, 7)

# 自相乘，得四萬四千一百步
田積步 = 田邊長 * 田邊長

# 以二百四十步除之，即得
畝數 = Fraction(田積步, 240)

# 100 畝為 1 頃
頃數 = 畝數 // 100
餘步 = 畝數 % 100

a = Fraction(頃數, 1) + Fraction(餘步, 100)  # 183/100 頃
b = 畝數 % 1 * 240  # 180 步
"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 147/80"""
