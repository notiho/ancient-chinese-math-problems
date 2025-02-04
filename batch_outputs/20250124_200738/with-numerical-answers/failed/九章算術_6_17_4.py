"""
今有五人分五錢，令上二人所得與下三人等。問︰各得幾何？
術曰：置錢錐行衰，并上二人為九，并下三人為六。六少於九，三。以三均加焉，副并為法。以所分錢乘未并者各自為實。實如法得一錢。
荅曰：甲得 a(=4/3)錢 ，乙得 b(=7/6)錢 ，丙得 c(=1)錢 ，丁得 d(=5/6)錢 ，戊得 e(=2/3)錢 。
"""

#----- content starts here -----
"""
Suppose there are 5 people dividing 5 qian. The condition is that the amount obtained by the first two people equals the amount obtained by the last three people.
Question: how much does each person get?

The procedure says: Arrange the qian in a tapered sequence.
Combine the first two people into 9 and the last three people into 6.
The difference between 6 and 9 is 3.
Distribute this difference equally and add it to the sequence.
Combine the adjusted sequence to form the divisor.
Multiply the total qian by the uncombined sequence to form the dividend for each person.
Divide the dividend by the divisor to obtain the amount of qian for each person.

Answer: Person A gets *a*(=4/3) qian, Person B gets *b*(=7/6) qian, Person C gets *c*(=1) qian, Person D gets *d*(=5/6) qian, Person E gets *e*(=2/3) qian.
"""

# 置錢錐行衰
錢序列 = [3, 2, 1, 1, 1]

# 并上二人為九
上二人 = sum(錢序列[:2])  # 3 + 2 = 5

# 并下三人為六
下三人 = sum(錢序列[2:])  # 1 + 1 + 1 = 3

# 六少於九，三
差 = 上二人 - 下三人  # 5 - 3 = 2

# 以三均加焉
調整 = 差 / 3  # 2 / 3
錢序列 = [錢 + 調整 for 錢 in 錢序列]

# 副并為法
法 = sum(錢序列)

# 以所分錢乘未并者各自為實
總錢 = 5
實 = [總錢 * 錢 for 錢 in 錢序列]

# 實如法得一錢
分配 = [Fraction(錢, 法) for 錢 in 實]

a, b, c, d, e = 分配  # 4/3, 7/6, 1, 5/6, 2/3#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
