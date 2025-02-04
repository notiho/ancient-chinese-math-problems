"""
今有牆田方周一千步。問：為田㡬何？
術曰：列田方周一千步以四除之得二百五十步自相乘得六萬二千五百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a square field with a perimeter of 1000 bu.
Question: how large is the area of the field?

The procedure says: Take the square field's perimeter of 1000 bu and divide it by 4, obtaining 250 bu (the length of one side).
Square this value, obtaining 62500 bu².
Divide this by the mu divisor (240 bu² per mu) to get the area in mu.
Finally, convert the result into qing (1 qing = 100 mu) and remaining bu.

Answer: *a* qing and *b* bu.
"""

from fractions import Fraction

# 方周一千步
方周 = 1000

# 以四除之得二百五十步
邊長 = 方周 / 4

# 自相乘得六萬二千五百步
積步 = 邊長 * 邊長

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得
畝數 = Fraction(積步, 畝法)

# 轉換為頃與剩餘步
頃 = 畝數 // 100  # 每 100 畝為 1 頃
剩餘畝 = 畝數 % 100

a = int(頃)
b = 剩餘畝

# Answer: a qing and b mu
a, b#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
