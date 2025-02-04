"""
今有五人分五錢令上二人所得與下三人等問各得幾何
術曰置錢錐行衰并上二人為九并下三人為六六少於九三以三均加焉副并為法以所分錢乘未并者各自為實實如法得一錢
荅曰甲得 a錢 乙得 b錢 丙得 c錢 丁得 d錢 戊得 e錢 
"""

#----- content starts here -----
"""
Suppose there are 5 people dividing 5 qian (units of money). 
The rule is that the amount received by the first two people (the upper group) is equal to the amount received by the last three people (the lower group).
Question: how much does each person receive?

The procedure says: Arrange the qian in a tapered sequence (weights decreasing). 
Add the weights of the first two people, obtaining 9. 
Add the weights of the last three people, obtaining 6. 
Since 6 is less than 9, add 3 to balance it. 
Combine all weights into a divisor. 
Multiply the total qian by the individual weights (before combining), obtaining the dividends. 
Divide each dividend by the divisor to find the amount of qian each person receives.

Answer: Person A receives *a* qian, Person B receives *b* qian, Person C receives *c* qian, Person D receives *d* qian, Person E receives *e* qian.
"""

# 置錢錐行衰
權重 = [5, 4, 2, 2, 2]  # Weights for each person (A, B, C, D, E)

# 并上二人為九
上二人 = sum(權重[:2])  # Sum of weights for the first two people

# 并下三人為六
下三人 = sum(權重[2:])  # Sum of weights for the last three people

# 六少於九，三以三均加焉
調整 = 上二人 - 下三人  # Difference between the two groups
權重[2:] = [w + 調整 // 3 for w in 权重[2:]]  # Adjust the weights of the last three people

# 副并為法
法 = sum(權重)  # Total weight (divisor)

# 以所分錢乘未并者，各自為實
所分錢 = 5  # Total qian to be divided
實 = [所分錢 * w for w in 權重]  # Dividends for each person

# 實如法得一錢
a, b, c, d, e = [Fraction(s, 法) for s in 實]  # Divide each dividend by the total weight

# Final result
a, b, c, d, e#----- content ends here -----

"""
Code error: name '权重' is not defined"""
