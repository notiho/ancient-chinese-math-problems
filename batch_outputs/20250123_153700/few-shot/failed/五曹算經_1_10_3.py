"""
今有田桑生中央從隅至桑一百四十七步。問：為田㡬何？
術曰：列一百四十七步以二乘之得二百九十四步以五乘之得一千四百七十步以七除之得二百一十步自相乘得四萬四千一百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

"""
Suppose there is a square field with a mulberry tree in the center. The distance from one corner of the field to the mulberry tree is 147 bu.
Question: how large is the field?

The procedure says: Take 147 bu, multiply it by 2, obtaining 294 bu.
Multiply this by 5, obtaining 1470 bu.
Divide this by 7, obtaining 210 bu.
Square this value, obtaining 44100 bu.
Divide this by the mu-divisor (240 bu), obtaining the area in mu.
100 mu make 1 qing.

Answer: *a* qing and *b* bu.
"""

from fractions import Fraction

# 中央從隅至桑一百四十七步
隅至桑 = 147

# 列一百四十七步以二乘之得二百九十四步
步_二倍 = 2 * 隅至桑

# 以五乘之得一千四百七十步
步_五倍 = 5 * 步_二倍

# 以七除之得二百一十步
步_七分之一 = Fraction(步_五倍, 7)

# 自相乘得四萬四千一百步
積步 = 步_七分之一 * 步_七分之一

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 100畝為1頃
頃 = 畝數 // 100
餘步 = 畝數 % 100

a = int(頃)
b = 餘步
"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 1
Variable 'b' has wrong value. Expected: 180, Actual: 335/4"""
