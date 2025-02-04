"""
今有五人分五錢令上二人所得與下三人等問各得幾何
術曰置錢錐行衰并上二人為九并下三人為六六少於九三以三均加焉副并為法以所分錢乘未并者各自為實實如法得一錢
荅曰甲得 a錢 乙得 b錢 丙得 c錢 丁得 d錢 戊得 e錢 
"""

#----- content starts here -----
"""
Suppose there are 5 people dividing 5 qian (units of money). 
The top two people together should receive the same amount as the bottom three people together.
Question: how much does each person receive?

The procedure says: Arrange the qian in a tapered sequence (decreasing weights).
Add the weights of the top two people, obtaining 9.
Add the weights of the bottom three people, obtaining 6.
Since 6 is less than 9, add 3 equally to the bottom three people's weights.
Add all the weights together to obtain the divisor.
Multiply the total amount of qian by the individual weights (before summing).
Divide each result by the divisor to obtain the amount of qian for each person.

The answer says: Jia gets *a* qian, Yi gets *b* qian, Bing gets *c* qian, Ding gets *d* qian, Wu gets *e* qian.
"""

# Initial weights for the five people in a tapered sequence
weights = [5, 4, 2, 2, 2]

# Add the weights of the top two people (5 + 4 = 9)
top_two_sum = weights[0] + weights[1]

# Add the weights of the bottom three people (2 + 2 + 2 = 6)
bottom_three_sum = sum(weights[2:])

# Since 6 < 9, add 3 equally to the bottom three people's weights
adjustment = 3
weights[2:] = [w + 1 for w in weights[2:]]

# Add all weights together to obtain the divisor
divisor = sum(weights)

# Total amount of qian to be divided
total_qian = 5

# Multiply the total amount of qian by the individual weights
# and divide by the divisor to calculate each person's share
a, b, c, d, e = [Fraction(total_qian * w, divisor) for w in weights]#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4/3, Actual: 25/18
Variable 'b' has wrong value. Expected: 7/6, Actual: 10/9
Variable 'c' has wrong value. Expected: 1, Actual: 5/6
Variable 'e' has wrong value. Expected: 2/3, Actual: 5/6"""
