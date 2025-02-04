"""
今有五人分五錢，令上二人所得與下三人等。問︰各得幾何？
術曰：置錢錐行衰，并上二人為九，并下三人為六。六少於九，三。以三均加焉，副并為法。以所分錢乘未并者各自為實。實如法得一錢。
荅曰：甲得 a錢 ，乙得 b錢 ，丙得 c錢 ，丁得 d錢 ，戊得 e錢 。
"""

#----- content starts here -----
"""
Suppose there are 5 people dividing 5 qian (units of money). 
The condition is that the amount received by the first two people (the upper two) is equal to the amount received by the last three people (the lower three).
Question: how much does each person receive?

The procedure says: Arrange the money in a tapered sequence decreasing by rank.
Combine the upper two people's shares into 9, and the lower three people's shares into 6.
The difference between 6 and 9 is 3. 
Distribute this difference equally among all, and add it back to the shares.
The total sum of all shares becomes the divisor.
Multiply the total money by the uncombined shares to get the dividend for each person.
Divide the dividend by the divisor to get the amount of money for each person.

Answer: Person 1 (甲) gets *a* qian, Person 2 (乙) gets *b* qian, Person 3 (丙) gets *c* qian, Person 4 (丁) gets *d* qian, and Person 5 (戊) gets *e* qian.
"""

from fractions import Fraction

# Total money to be divided
total_money = 5

# Initial tapered sequence of shares
shares = [5, 4, 3, 2, 1]

# Combine the upper two and lower three
upper_two = shares[0] + shares[1]  # 5 + 4 = 9
lower_three = shares[2] + shares[3] + shares[4]  # 3 + 2 + 1 = 6

# Difference between upper two and lower three
difference = upper_two - lower_three  # 9 - 6 = 3

# Distribute the difference equally among all and adjust shares
adjusted_shares = [share + Fraction(difference, len(shares)) for share in shares]

# Calculate the divisor (sum of adjusted shares)
divisor = sum(adjusted_shares)

# Calculate the amount each person gets
results = [Fraction(total_money) * share / divisor for share in adjusted_shares]

# Assign results to each person
a, b, c, d, e = results

# Output
a, b, c, d, e#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4/3, Actual: 14/9
Variable 'b' has wrong value. Expected: 7/6, Actual: 23/18
Variable 'd' has wrong value. Expected: 5/6, Actual: 13/18
Variable 'e' has wrong value. Expected: 2/3, Actual: 4/9"""
