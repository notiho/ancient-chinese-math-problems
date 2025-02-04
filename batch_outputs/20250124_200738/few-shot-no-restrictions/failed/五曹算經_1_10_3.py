"""
今有田桑生中央從隅至桑一百四十七步。問：為田㡬何？
術曰：列一百四十七步以二乘之得二百九十四步以五乘之得一千四百七十步以七除之得二百一十步自相乘得四萬四千一百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a square field with a mulberry tree at the center. The distance from a corner of the field to the mulberry tree is 147 bu.
Question: how large is the field?

The procedure says: Take the 147 bu, multiply it by 2, obtaining 294 bu. Multiply it by 5, obtaining 1470 bu. Divide it by 7, obtaining 210 bu. Square this value, obtaining 44100 bu. Divide it by the mu-divisor (240 bu), obtaining the field size in mu.

Answer: *a* qing and *b* bu.
"""

from fractions import Fraction

# 從隅至桑一百四十七步
從隅至桑 = 147

# 列一百四十七步以二乘之得二百九十四步
步_1 = 2 * 從隅至桑

# 以五乘之得一千四百七十步
步_2 = 5 * 步_1

# 以七除之得二百一十步
步_3 = Fraction(步_2, 7)

# 自相乘得四萬四千一百步
積步 = 步_3 ** 2

# 以畝法除之即得
畝法 = 240
畝數 = Fraction(積步, 畝法)

# 百畝為一頃
頃 = 畝數 // 100
剩餘步 = 畝數 % 100

# 答案
a = int(頃)
b = 剩餘步
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 1
Variable 'b' has wrong value. Expected: 180, Actual: 335/4"""
