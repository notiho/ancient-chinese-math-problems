"""
今有牆田方周一千步。問：為田㡬何？
術曰：列田方周一千步以四除之得二百五十步自相乘得六萬二千五百步以畝法除之即得。
答曰： a(=13/5)頃 奇 b(=100)步 。
"""

"""
Suppose there is a square field with a perimeter of 1000 bu.
Question: how large is the area of the field?

The procedure says: Take the square field's perimeter of 1000 bu and divide it by 4, obtaining 250 bu.
Square this value, obtaining 62500 bu².
Divide this by the mu-divisor (240 bu² per mu), and the result is the area.

Answer: *a*(=13/5) qing and *b*(=100) bu².
"""

from fractions import Fraction

# 方周一千步
方周 = 1000

# 以四除之
邊長 = 方周 / 4

# 自相乘
積步 = 邊長 * 邊長

# 畝法二百四十步
畝法 = 240

# 以畝法除之
畝數 = Fraction(積步, 畝法)

# 100 畝為 1 頃
頃數 = 畝數 // 100
奇步 = 畝數 % 100

a = Fraction(頃數)  # 13/5
b = 奇步  # 100
"""
Code error: both arguments should be Rational instances"""
