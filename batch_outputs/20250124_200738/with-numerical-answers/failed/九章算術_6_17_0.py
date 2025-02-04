"""
今有五人分五錢，令上二人所得與下三人等。問︰各得幾何？
術曰：置錢錐行衰，并上二人為九，并下三人為六。六少於九，三。以三均加焉，副并為法。以所分錢乘未并者各自為實。實如法得一錢。
荅曰：甲得 a(=4/3)錢 ，乙得 b(=7/6)錢 ，丙得 c(=1)錢 ，丁得 d(=5/6)錢 ，戊得 e(=2/3)錢 。
"""

#----- content starts here -----
"""
Suppose there are 5 people dividing 5 qian, such that the amount received by the first two people is equal to the amount received by the last three people.
Question: how much does each person receive?

The procedure says: Arrange the qian in a tapering sequence. Combine the first two people, obtaining 9. Combine the last three people, obtaining 6. The difference between 6 and 9 is 3. Distribute this difference equally, adding it to each. Combine all as the divisor. Multiply the total qian by the uncombined values, obtaining the dividend for each. Divide the dividend by the divisor to obtain the amount of qian for each person.

Answer: Person 1 (甲) gets *a*(=4/3) qian, Person 2 (乙) gets *b*(=7/6) qian, Person 3 (丙) gets *c*(=1) qian, Person 4 (丁) gets *d*(=5/6) qian, Person 5 (戊) gets *e*(=2/3) qian.
"""

# 置錢錐行衰
錢序 = [5, 4, 3, 2, 1]

# 并上二人為九
上二人 = 錢序[0] + 錢序[1]

# 并下三人為六
下三人 = 錢序[2] + 錢序[3] + 錢序[4]

# 六少於九，三
差 = 上二人 - 下三人

# 以三均加焉
錢序 = [x + 差 for x in 錢序]

# 副并為法
法 = sum(錢序)

# 以所分錢乘未并者各自為實
所分錢 = 5
實 = [所分錢 * x for x in 錢序]

# 實如法得一錢
a, b, c, d, e = [Fraction(x, 法) for x in 实] # 4/3, 7/6, 1, 5/6, 2/3#----- content ends here -----

"""
Code error: name '实' is not defined"""
