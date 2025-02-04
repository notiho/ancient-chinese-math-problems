"""
今有五人分五錢，令上二人所得與下三人等。問︰各得幾何？
術曰：置錢錐行衰，并上二人為九，并下三人為六。六少於九，三。以三均加焉，副并為法。以所分錢乘未并者各自為實。實如法得一錢。
荅曰：甲得 a錢 ，乙得 b錢 ，丙得 c錢 ，丁得 d錢 ，戊得 e錢 。
"""

#----- content starts here -----
"""
Suppose there are 5 people dividing 5 qian, such that the amount obtained by the first two people equals the amount obtained by the last three people.
Question: how much does each person get?

The procedure says: Arrange the qian in a tapering sequence. Combine the first two people into 9, and the last three people into 6.
The difference between 6 and 9 is 3. Add this difference evenly to balance them, and combine the totals to form the divisor.
Multiply the total qian by the uncombined values for each person to form the dividend.
Divide the dividend by the divisor to obtain the amount of qian for each person.

Answer: Person A gets *a* qian, Person B gets *b* qian, Person C gets *c* qian, Person D gets *d* qian, and Person E gets *e* qian.
"""

# Total qian to be divided
總錢 = 5

# Arrange the tapering sequence for the five people
分配 = [5, 4, 3, 2, 1]

# Combine the first two people (5 + 4 = 9) and the last three people (3 + 2 + 1 = 6)
上二人 = 分配[0] + 分配[1]  # 9
下三人 = 分配[2] + 分配[3] + 分配[4]  # 6

# The difference between 6 and 9 is 3
差 = 上二人 - 下三人  # 3

# Add this difference evenly to balance them
平衡加 = 差

# Combine the totals to form the divisor
法 = sum(分配) + 平衡加  # 5 + 4 + 3 + 2 + 1 + 3 = 18

# Multiply the total qian by the uncombined values for each person to form the dividend
實 = [總錢 * i for i in 分配]

# Divide the dividend by the divisor to obtain the amount of qian for each person
a, b, c, d, e = [Fraction(i, 法) for i in 實]#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4/3, Actual: 25/18
Variable 'b' has wrong value. Expected: 7/6, Actual: 10/9
Variable 'c' has wrong value. Expected: 1, Actual: 5/6
Variable 'd' has wrong value. Expected: 5/6, Actual: 5/9
Variable 'e' has wrong value. Expected: 2/3, Actual: 5/18"""
