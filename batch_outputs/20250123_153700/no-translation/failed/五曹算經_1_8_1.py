"""
今有牆田方周一千步。問：為田㡬何？
術曰：列田方周一千步以四除之得二百五十步自相乘得六萬二千五百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""


# 田方周一千步
方周 = 1000

# 列田方周一千步以四除之
邊長 = Fraction(方周, 4)

# 得二百五十步自相乘
積步 = 邊長 * 邊長

# 畝法二百四十步
畝法 = 240

# 以畝法除之即得畝數
畝數 = Fraction(積步, 畝法)

# 百畝為一頃
頃 = 畝數 // 100
奇步 = 畝數 % 100

a = int(頃)
b = 奇步
"""
Variable 'a' has wrong value. Expected: 13/5, Actual: 2
Variable 'b' has wrong value. Expected: 100, Actual: 725/12"""
