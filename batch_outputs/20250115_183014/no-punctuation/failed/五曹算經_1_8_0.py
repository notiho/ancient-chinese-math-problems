"""
今有牆田方周一千步問為田㡬何
術曰列田方周一千步以四除之得二百五十步自相乘得六萬二千五百步以畝法除之即得
答曰 a頃 奇 b步 
"""

"""
Suppose there is a square field with a perimeter of 1000 bu.
Question: how large is the field?

The procedure says: Take the square field's perimeter of 1000 bu and divide it by 4, obtaining 250 bu.
Square this value, obtaining 62500 bu².
Divide it by the mu-divisor, 240, to obtain the number of mu.
100 mu make 1 qing.

Answer: *a* qing and *b* bu.
"""

# 田方周一千步
周 = 1000

# 以四除之，得二百五十步
邊長 = 周 / 4

# 自相乘，得六萬二千五百步
積步 = 邊長 * 邊長

# 畝法二百四十步
畝法 = 240

# 以畝法除之，即得畝數
畝數 = Fraction(積步, 畝法)

# 100畝為1頃
a = 畝數 // 100  # 整數部分為頃數
b = 畝數 % 100   # 餘數部分為奇步數
"""
Code error: both arguments should be Rational instances"""
