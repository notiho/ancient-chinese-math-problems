"""
今有五人分五錢令上二人所得與下三人等問各得幾何
術曰置錢錐行衰并上二人為九并下三人為六六少於九三以三均加焉副并為法以所分錢乘未并者各自為實實如法得一錢
荅曰甲得 a錢 乙得 b錢 丙得 c錢 丁得 d錢 戊得 e錢 
"""

"""
Suppose there are 5 people dividing 5 qian (coins). The sum of the amounts obtained by the first two people must equal the sum of the amounts obtained by the last three people.
Question: how much does each person get?

The procedure says: Arrange the qian in a tapered sequence (decreasing order).
Add the first two people, obtaining 9.
Add the last three people, obtaining 6.
Since 6 is less than 9 by 3, divide this difference by 3 and distribute it evenly.
Add this adjustment to the sequence.
The adjusted sequence becomes the divisor.
Multiply the total qian by the unadjusted sequence for each person, obtaining the dividend.
Divide each dividend by the divisor, obtaining the amount of qian for each person.

Answer: Person A gets *a* qian, Person B gets *b* qian, Person C gets *c* qian, Person D gets *d* qian, Person E gets *e* qian.
"""

# 置錢錐行衰
錢序列 = [5, 4, 3, 2, 1]

# 并上二人為九
上二人和 = 錢序列[0] + 錢序列[1]

# 并下三人為六
下三人和 = 錢序列[2] + 錢序列[3] + 錢序列[4]

# 六少於九三，以三均加焉
差 = 上二人和 - 下三人和
調整 = 差 // 3
錢序列 = [x - 調整 for x in 錢序列]

# 副并為法
法 = sum(錢序列)

# 以所分錢乘未并者
所分錢 = 5
實 = [所分錢 * x for x in 錢序列]

# 各自為實，實如法得一錢
a, b, c, d, e = [Fraction(x, 法) for x in 実]
"""
Code error: name '実' is not defined"""
