"""
今有五人分五錢，令上二人所得與下三人等。問︰各得幾何？
術曰：置錢錐行衰，并上二人為九，并下三人為六。六少於九，三。以三均加焉，副并為法。以所分錢乘未并者各自為實。實如法得一錢。
荅曰：甲得 a錢 ，乙得 b錢 ，丙得 c錢 ，丁得 d錢 ，戊得 e錢 。
"""

#----- content starts here -----
"""
Suppose there are 5 people dividing 5 qian, such that the amount obtained by the first two people equals the amount obtained by the last three people.
Question: how much does each person get?

The procedure says: Arrange the qian in a tapered sequence [weights decreasing].
Combine the weights of the first two people, obtaining 9.
Combine the weights of the last three people, obtaining 6.
The difference between 6 and 9 is 3.
Distribute this difference equally, adding it to the weights.
Combine all weights to obtain the divisor.
Multiply the total qian by the individual weights to obtain the dividends.
Divide the dividends by the divisor to obtain the amount of qian for each person.

Answer: Person A gets *a* qian, Person B gets *b* qian, Person C gets *c* qian, Person D gets *d* qian, and Person E gets *e* qian.
"""

# Initial weights for the five people
weights = [5, 4, 3, 2, 1]

# Combine weights for the first two people and the last three people
上二人 = weights[0] + weights[1]  # 5 + 4 = 9
下三人 = weights[2] + weights[3] + weights[4]  # 3 + 2 + 1 = 6

# Difference between the two groups
差 = 上二人 - 下三人  # 9 - 6 = 3

# Distribute the difference equally and adjust weights
weights = [w + 差 // len(weights) for w in weights]  # Add 3/5 to each weight

# Combine all weights to obtain the divisor
法 = sum(weights)

# Total qian to be divided
總錢 = 5

# Calculate the amount of qian for each person
實 = [總錢 * w for w in weights]
a, b, c, d, e = [Fraction(s, 法) for s in 實]#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4/3, Actual: 5/3
Variable 'b' has wrong value. Expected: 7/6, Actual: 4/3
Variable 'd' has wrong value. Expected: 5/6, Actual: 2/3
Variable 'e' has wrong value. Expected: 2/3, Actual: 1/3"""
