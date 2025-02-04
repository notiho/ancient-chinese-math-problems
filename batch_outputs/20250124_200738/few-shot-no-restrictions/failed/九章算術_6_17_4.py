"""
今有五人分五錢，令上二人所得與下三人等。問︰各得幾何？
術曰：置錢錐行衰，并上二人為九，并下三人為六。六少於九，三。以三均加焉，副并為法。以所分錢乘未并者各自為實。實如法得一錢。
荅曰：甲得 a錢 ，乙得 b錢 ，丙得 c錢 ，丁得 d錢 ，戊得 e錢 。
"""

#----- content starts here -----
"""
Suppose there are five people dividing five qian (units of money). 
The condition is that the amount received by the first two people (the "upper two") is equal to the amount received by the last three people (the "lower three").
Question: how much does each person receive?

The procedure says: Arrange the qian in a decreasing sequence. Combine the shares of the upper two people into 9 and the lower three people into 6. 
The difference between 6 and 9 is 3. Distribute this difference evenly among the five people, and add it to their shares. 
The combined total becomes the divisor. Multiply the total qian by the uncombined shares of each person to get the dividend. 
Divide the dividend by the divisor to get the amount of qian for each person.

Answer: Person A gets *a* qian, Person B gets *b* qian, Person C gets *c* qian, Person D gets *d* qian, and Person E gets *e* qian.
"""

from fractions import Fraction

# Total money to be divided
total_qian = 5

# Initial shares in a decreasing sequence
shares = [5, 4, 3, 2, 1]

# Combine the shares of the upper two (first two people) and the lower three (last three people)
upper_two = shares[0] + shares[1]  # 5 + 4 = 9
lower_three = shares[2] + shares[3] + shares[4]  # 3 + 2 + 1 = 6

# Difference between upper two and lower three
difference = upper_two - lower_three  # 9 - 6 = 3

# Distribute the difference evenly among all five people
adjusted_shares = [share + Fraction(difference, len(shares)) for share in shares]

# Combine the adjusted shares to get the divisor
divisor = sum(adjusted_shares)

# Calculate the dividend for each person
dividends = [total_qian * share for share in adjusted_shares]

# Divide each dividend by the divisor to get the final amount for each person
final_shares = [Fraction(dividend, divisor) for dividend in dividends]

# Assign the results to each person
a, b, c, d, e = final_shares

# Output the results
a, b, c, d, e#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4/3, Actual: 14/9
Variable 'b' has wrong value. Expected: 7/6, Actual: 23/18
Variable 'd' has wrong value. Expected: 5/6, Actual: 13/18
Variable 'e' has wrong value. Expected: 2/3, Actual: 4/9"""
