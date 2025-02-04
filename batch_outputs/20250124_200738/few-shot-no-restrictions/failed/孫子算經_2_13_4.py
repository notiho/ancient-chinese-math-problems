"""
今有方田桑生中央，從角至桑，一百四十七步。問：為田幾何？
術曰：置角至桑一百四十七步，倍之，得二百九十四步，以五乘之，得一千四百七十步，以七除之，得二百一十步，自相乘，得四萬四千一百步，以二百四十步除之，即得。
答曰： a頃 ，奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a square field with a mulberry tree growing at its center. 
The distance from a corner of the field to the mulberry tree is 147 bu.
Question: how large is the field?

The procedure says: Place the distance from the corner to the mulberry tree as 147 bu.
Double it, obtaining 294 bu.
Multiply it by 5, obtaining 1470 bu.
Divide it by 7, obtaining 210 bu.
Square this, obtaining 44100 bu.
Divide it by 240 bu to obtain the area in mu.

Answer: *a* qing, with a remainder of *b* bu.
"""

from fractions import Fraction

# 從角至桑，一百四十七步
角至桑 = 147

# 倍之，得二百九十四步
倍步 = 2 * 角至桑

# 以五乘之，得一千四百七十步
乘五步 = 5 * 倍步

# 以七除之，得二百一十步
邊長 = Fraction(乘五步, 7)

# 自相乘，得四萬四千一百步
田積步 = 邊長 * 邊長

# 以二百四十步除之，即得
畝法 = 240
田積畝 = Fraction(田積步, 畝法)

# 百畝為一頃
畝每頃 = 100
田積頃 = int(田積畝 // 畝每頃)  # 整數部分為頃數
田積餘步 = 田積畝 % 畝每頃  # 餘數為奇步數

a = 田積頃
b = 田積餘步

# Output the results
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 1
Variable 'b' has wrong value. Expected: 180, Actual: 335/4"""
