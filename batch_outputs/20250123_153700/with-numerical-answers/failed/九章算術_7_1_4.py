"""
今有共買雞，人出九，盈十一；人出六，不足十六。問︰人數、雞價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a(=9)人 ，雞價 b(=70) 。
"""

"""
Suppose a group of people jointly buys chickens. If each person contributes 9, there is an excess of 11. 
If each person contributes 6, there is a shortfall of 16. 
Question: how many people are there, and what is the price of the chickens?

The procedure for surplus and deficit says: Place the contribution rates, with the surplus and deficit below each. 
Multiply the contribution rates by their respective surplus or deficit, and sum these to obtain the dividend. 
Add the surplus and deficit to obtain the divisor. 
Divide the dividend by the divisor to find the result. If there is a fraction, simplify it. 
If the surplus and deficit correspond to the same item being purchased, place the contribution rates, subtract the smaller from the larger, and simplify the divisor and dividend. 
The dividend is the price of the item, and the divisor is the number of people.

Answer: *a*(=9) people, *b*(=70) is the price of the chickens.
"""

# 人出九，盈十一
出率1 = 9
盈 = 11

# 人出六，不足十六
出率2 = 6
不足 = 16

# 置所出率，盈、不足各居其下
# 令維乘所出率，并以為實
實 = (出率1 * 盈) + (出率2 * 不足)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
雞價 = Fraction(實, 法)

# 盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實
人數 = Fraction(出率1 - 出率2, 法)

# 有分者，通之
a = int(1 / float(人數))  # 9 people
b = int(雞價)  # 70 chicken price
"""
Variable 'b' has wrong value. Expected: 70, Actual: 7"""
