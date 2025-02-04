"""
今有田桑生中央從隅至桑一百四十七步。問：為田㡬何？
術曰：列一百四十七步以二乘之得二百九十四步以五乘之得一千四百七十步以七除之得二百一十步自相乘得四萬四千一百步以畝法除之即得。
答曰： a(=183/100)頃 奇 b(=180)步 。
"""

#----- content starts here -----
"""
Suppose there is a square field with a mulberry tree growing in the center. The distance from a corner of the field to the mulberry tree is 147 bu.
Question: how large is the field?

The procedure says: Take 147 bu, multiply it by 2, obtaining 294 bu. Multiply it by 5, obtaining 1470 bu. Divide it by 7, obtaining 210 bu. Square this, obtaining 44100 bu. Divide it by the mu-divisor, obtaining the result.

Answer: *a*(=183/100) qing and *b*(=180) bu.
"""

from fractions import Fraction

# 中央從隅至桑一百四十七步
從隅至桑 = 147

# 列一百四十七步以二乘之得二百九十四步
步_二倍 = 2 * 從隅至桑

# 以五乘之得一千四百七十步
步_五倍 = 5 * 步_二倍

# 以七除之得二百一十步
步_七分之一 = Fraction(步_五倍, 7)

# 自相乘得四萬四千一百步
積步 = 步_七分之一 ** 2

# 以畝法除之即得
畝法 = 240  # 1 畝 = 240 步
畝數 = Fraction(積步, 畝法)

# Convert 畝數 to 頃 and 步
畝每頃 = 100  # 1 頃 = 100 畝
頃數 = 畝數 // 畝每頃
剩餘畝 = 畝數 % 畝每頃
步數 = 剩餘畝 * 畝法

a = 頃數 + Fraction(剩餘畝, 畝每頃)  # 183/100 頃
b = 步數  # 180 步#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 147/80
Variable 'b' has wrong value. Expected: 180, Actual: 20100"""
