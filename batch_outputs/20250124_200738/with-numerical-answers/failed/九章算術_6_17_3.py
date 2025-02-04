"""
今有五人分五錢，令上二人所得與下三人等。問︰各得幾何？
術曰：置錢錐行衰，并上二人為九，并下三人為六。六少於九，三。以三均加焉，副并為法。以所分錢乘未并者各自為實。實如法得一錢。
荅曰：甲得 a(=4/3)錢 ，乙得 b(=7/6)錢 ，丙得 c(=1)錢 ，丁得 d(=5/6)錢 ，戊得 e(=2/3)錢 。
"""

#----- content starts here -----
"""
Suppose there are five people dividing five qian, with the condition that the total amount received by the first two people equals the total amount received by the last three people.
Question: how much does each person receive?

The procedure says: Arrange the qian in a tapering sequence.
Combine the first two people, obtaining 9, and combine the last three people, obtaining 6.
The difference between 6 and 9 is 3.
Distribute this difference equally among the five people, adding it to the tapering sequence.
Combine the adjusted sequence to obtain the divisor.
Multiply the total qian by the unadjusted sequence to obtain the dividend for each person.
Divide the dividend by the divisor to determine the amount each person receives.

Answer: Person 1 (甲) receives *a*(=4/3) qian, Person 2 (乙) receives *b*(=7/6) qian, Person 3 (丙) receives *c*(=1) qian, Person 4 (丁) receives *d*(=5/6) qian, and Person 5 (戊) receives *e*(=2/3) qian.
"""

# 置錢錐行衰
錢序列 = [5, 4, 3, 2, 1]

# 并上二人為九
上二人 = sum(錢序列[:2])  # 5 + 4 = 9

# 并下三人為六
下三人 = sum(錢序列[2:])  # 3 + 2 + 1 = 6

# 六少於九，三
差值 = 上二人 - 下三人  # 9 - 6 = 3

# 以三均加焉
調整值 = Fraction(差值, len(錢序列))  # 3 / 5
調整後序列 = [x + 調整值 for x in 錢序列]

# 副并為法
法 = sum(調整後序列)

# 以所分錢乘未并者各自為實
所分錢 = 5
實 = [所分錢 * x for x in 調整後序列]

# 實如法得一錢
分配結果 = [Fraction(x, 法) for x in 実]

# 分配結果
a, b, c, d, e = 分配結果  # 4/3, 7/6, 1, 5/6, 2/3#----- content ends here -----

"""
Code error: name '実' is not defined"""
