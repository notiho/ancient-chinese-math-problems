"""
今有五人分五錢，令上二人所得與下三人等。問︰各得幾何？
術曰：置錢錐行衰，并上二人為九，并下三人為六。六少於九，三。以三均加焉，副并為法。以所分錢乘未并者各自為實。實如法得一錢。
荅曰：甲得 a錢 ，乙得 b錢 ，丙得 c錢 ，丁得 d錢 ，戊得 e錢 。
"""

#----- content starts here -----
"""
Suppose there are 5 people dividing 5 qian, such that the amount obtained by the first two people equals the amount obtained by the last three people.
Question: how much does each person get?

The procedure says: Arrange the qian in a tapering sequence. Combine the first two people into 9, and combine the last three people into 6.
The difference between 6 and 9 is 3. Distribute this difference equally, and add it to each. Combine the auxiliary values to form the divisor.
Multiply the total qian by the uncombined values for each person to form the dividend.
Divide the dividend by the divisor to obtain the amount of qian for each person.

Answer: Person A gets *a* qian, Person B gets *b* qian, Person C gets *c* qian, Person D gets *d* qian, and Person E gets *e* qian.
"""

# 置錢錐行衰
錢分配 = [5, 4, 3, 2, 1]

# 并上二人為九
上二人 = 5 + 4

# 并下三人為六
下三人 = 3 + 2 + 1

# 六少於九，三
差額 = 上二人 - 下三人

# 以三均加焉
調整 = 差額 / len(錢分配)

# 副并為法
法 = sum(錢分配)

# 以所分錢乘未并者各自為實
總錢 = 5
實 = [總錢 * i for i in 錢分配]

# 實如法得一錢
a, b, c, d, e = [Fraction(i, 法) for i in 實]#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4/3, Actual: 5/3
Variable 'b' has wrong value. Expected: 7/6, Actual: 4/3
Variable 'd' has wrong value. Expected: 5/6, Actual: 2/3
Variable 'e' has wrong value. Expected: 2/3, Actual: 1/3"""
