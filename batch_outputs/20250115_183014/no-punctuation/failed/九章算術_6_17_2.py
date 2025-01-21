"""
今有五人分五錢令上二人所得與下三人等問各得幾何
術曰置錢錐行衰并上二人為九并下三人為六六少於九三以三均加焉副并為法以所分錢乘未并者各自為實實如法得一錢
荅曰甲得 a錢 乙得 b錢 丙得 c錢 丁得 d錢 戊得 e錢 
"""

"""
Suppose there are 5 people dividing 5 qian. It is required that the sum of the amounts obtained by the first two people equals the sum of the amounts obtained by the last three people.
Question: how much does each person get?

The procedure says: Arrange the qian in a tapered sequence, decreasing. 
Combine the first two people, obtaining 9. Combine the last three people, obtaining 6.
Since 6 is less than 9 by 3, distribute this difference equally among the three.
Add this adjustment to the auxiliary sequence, obtaining the divisor.
Multiply the total qian by the uncombined sequence, obtaining the dividend for each.
Divide the dividend by the divisor to obtain the amount of qian for each person.

The answer says: Jia gets *a* qian, Yi gets *b* qian, Bing gets *c* qian, Ding gets *d* qian, Wu gets *e* qian.
"""

# 置錢錐行衰
錢序列 = [5, 4, 3, 2, 1]

# 并上二人為九
上二人 = 錢序列[0] + 錢序列[1]

# 并下三人為六
下三人 = 錢序列[2] + 錢序列[3] + 錢序列[4]

# 六少於九三，以三均加焉
差額 = 上二人 - 下三人
調整 = 差額 / 3
錢序列[2] += 調整
錢序列[3] += 調整
錢序列[4] += 調整

# 副并為法
法 = sum(錢序列)

# 以所分錢乘未并者
所分錢 = 5
實 = [所分錢 * i for i in 錢序列]

# 各自為實，實如法得一錢
a, b, c, d, e = [Fraction(i, 法) for i in 實]
"""
Code error: both arguments should be Rational instances"""
