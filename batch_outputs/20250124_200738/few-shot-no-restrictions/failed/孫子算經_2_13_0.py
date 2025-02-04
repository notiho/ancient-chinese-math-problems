"""
今有方田桑生中央，從角至桑，一百四十七步。問：為田幾何？
術曰：置角至桑一百四十七步，倍之，得二百九十四步，以五乘之，得一千四百七十步，以七除之，得二百一十步，自相乘，得四萬四千一百步，以二百四十步除之，即得。
答曰： a頃 ，奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a square field with a mulberry tree growing at its center. The distance from a corner of the field to the mulberry tree is 147 bu.
Question: how large is the field?

The procedure says: Take the distance from the corner to the mulberry tree, 147 bu, and double it, obtaining 294 bu.
Multiply it by 5, obtaining 1470 bu.
Divide it by 7, obtaining 210 bu.
Square this value, obtaining 44100 bu.
Divide it by 240 bu (the mu divisor), obtaining the field size in mu.
Convert the result into qing and remaining bu.

Answer: *a* qing, with *b* bu remaining.
"""

from fractions import Fraction

# 角至桑一百四十七步
角至桑 = 147

# 倍之，得二百九十四步
倍步 = 2 * 角至桑

# 以五乘之，得一千四百七十步
乘五步 = 5 * 倍步

# 以七除之，得二百一十步
步長 = Fraction(乘五步, 7)

# 自相乘，得四萬四千一百步
積步 = 步長 ** 2

# 以二百四十步除之，即得畝數
畝法 = 240
畝數 = Fraction(積步, 畝法)

# 百畝為一頃
畝每頃 = 100
頃數 = 畝數 // 畝每頃
餘畝 = 畝數 % 畝每頃

# Convert remaining mu into bu
餘步 = Fraction(餘畝 * 畝法)

a = int(頃數)  # 整數部分為頃數
b = int(餘步)  # 餘數部分為步數

# Output the result
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 1
Variable 'b' has wrong value. Expected: 180, Actual: 20100"""
