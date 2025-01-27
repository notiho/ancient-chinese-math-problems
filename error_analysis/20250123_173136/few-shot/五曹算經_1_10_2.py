"""
今有田桑生中央從隅至桑一百四十七步。問：為田㡬何？
術曰：列一百四十七步以二乘之得二百九十四步以五乘之得一千四百七十步以七除之得二百一十步自相乘得四萬四千一百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

"""
Suppose there is a square field with a mulberry tree in the center. The distance from the corner of the field to the mulberry tree is 147 bu.
Question: how large is the field?

The procedure says: Take 147 bu, multiply it by 2, obtaining 294 bu. Multiply it by 5, obtaining 1470 bu. Divide it by 7, obtaining 210 bu. Square this value, obtaining 44100 bu. Divide it by the mu-divisor (240 bu), obtaining the area in mu.

The answer says: *a* qing and *b* bu.
"""

from fractions import Fraction

# 從隅至桑一百四十七步
隅至桑 = 147

# 以二乘之得二百九十四步
步二 = 隅至桑 * 2

# 以五乘之得一千四百七十步
步五 = 步二 * 5

# 以七除之得二百一十步
步七 = Fraction(步五, 7)

# 自相乘得四萬四千一百步
積步 = 步七 * 步七

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
#ERR: code error (fractions)
#畝數 = Fraction(積步, 畝法)
畝數 = 積步 // 畝法

# 百畝為一頃
#ERR: code error (fractions)
#頃 = 畝數 // 100
#奇步 = 畝數 % 100
頃 = Fraction(畝數, 100)
奇步 = 積步 % 畝法

#ERR: code error (fractions)
#a = int(頃)
a = 頃
b = 奇步
"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 1
Variable 'b' has wrong value. Expected: 180, Actual: 335/4"""
