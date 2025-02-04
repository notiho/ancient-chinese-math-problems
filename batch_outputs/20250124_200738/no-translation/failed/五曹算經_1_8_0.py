"""
今有牆田方周一千步。問：為田㡬何？
術曰：列田方周一千步以四除之得二百五十步自相乘得六萬二千五百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

#----- content starts here -----

# 田方周一千步
方周 = 1000

# 以四除之得二百五十步
邊長 = 方周 / 4

# 自相乘得六萬二千五百步
積步 = 邊長 * 邊長

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得畝數
畝數 = Fraction(積步, 畝法)

# 百畝為一頃
頃 = 畝數 // 100
剩餘畝 = 畝數 % 100

a = int(頃)
b = 剩餘畝#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
