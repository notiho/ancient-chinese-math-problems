"""
今有田桑生中央從隅至桑一百四十七步問為田㡬何
術曰列一百四十七步以二乘之得二百九十四步以五乘之得一千四百七十步以七除之得二百一十步自相乘得四萬四千一百步以畝法除之即得
答曰 a頃 奇 b步 
"""

#----- content starts here -----
"""
Suppose there is a mulberry tree in the center of a field. From the corner to the mulberry tree, it is 147 bu.
Question: how large is the field?

The procedure says: Take 147 bu and multiply it by 2, obtaining 294 bu.
Multiply it by 5, obtaining 1470 bu.
Divide it by 7, obtaining 210 bu.
Square this result, obtaining 44100 bu.
Divide it by the mu-divisor (240 bu), obtaining the result.

Answer: *a* qing and *b* bu.
"""

from fractions import Fraction

# 從隅至桑一百四十七步
隅至桑 = 147

# 以二乘之，得二百九十四步
步1 = 隅至桑 * 2

# 以五乘之，得一千四百七十步
步2 = 步1 * 5

# 以七除之，得二百一十步
步3 = Fraction(步2, 7)

# 自相乘，得四萬四千一百步
積步 = 步3 * 步3

# 以畝法除之，即得
畝法 = 240
畝數 = Fraction(積步, 畝法)

# 百畝為一頃
頃 = 畝數 // 100
奇步 = 畝數 % 100

a = int(頃)
b = 奇步
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 1
Variable 'b' has wrong value. Expected: 180, Actual: 335/4"""
