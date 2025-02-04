"""
今有五人分五錢，令上二人所得與下三人等。問︰各得幾何？
術曰：置錢錐行衰，并上二人為九，并下三人為六。六少於九，三。以三均加焉，副并為法。以所分錢乘未并者各自為實。實如法得一錢。
荅曰：甲得 a(=4/3)錢 ，乙得 b(=7/6)錢 ，丙得 c(=1)錢 ，丁得 d(=5/6)錢 ，戊得 e(=2/3)錢 。
"""

"""
Suppose there are 5 people dividing 5 qian, such that the amount obtained by the first two people equals the amount obtained by the last three people.
Question: how much does each person get?

The procedure says: Arrange the qian in a tapered sequence decreasing by rank.
Combine the first two people, obtaining 9. Combine the last three people, obtaining 6.
The difference between 6 and 9 is 3. Distribute this difference equally, adding it to the sequence.
Combine all as the divisor.
Multiply the total qian by the uncombined sequence, each becoming its own dividend.
Divide the dividends by the divisor to obtain the amount of qian for each person.

The answer says: Person A gets *a*(=4/3) qian, Person B gets *b*(=7/6) qian, Person C gets *c*(=1) qian, Person D gets *d*(=5/6) qian, and Person E gets *e*(=2/3) qian.
"""

# Initial tapered sequence for the 5 people
錢序列 = [5, 4, 3, 2, 1]

# Combine the first two people and the last three people
上二人 = sum(錢序列[:2])  # 5 + 4 = 9
下三人 = sum(錢序列[2:])  # 3 + 2 + 1 = 6

# Difference between the two groups
差 = 上二人 - 下三人  # 9 - 6 = 3

# Distribute the difference equally across the sequence
錢序列 = [x + 差 / len(錢序列) for x in 錢序列]  # Add 3/5 to each element

# Combine all as the divisor (法)
法 = sum(錢序列)

# Multiply the total qian (5) by the adjusted sequence to get the dividends (實)
總錢 = 5
實 = [總錢 * x for x in 錢序列]

# Divide each dividend by the divisor to get the amount of qian for each person
a, b, c, d, e = [Fraction(x, 法) for x in 實]  # 4/3, 7/6, 1, 5/6, 2/3
"""
Code error: both arguments should be Rational instances"""
