"""
今有共買雞，人出九，盈十一；人出六，不足十六。問︰人數、雞價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，雞價 b 。
"""

"""
Suppose a group of people collectively buys chickens. 
When each person contributes 9, there is an excess of 11. 
When each person contributes 6, there is a shortfall of 16. 
Question: how many people are there, and what is the price of the chickens?

The procedure for surplus and deficit says: Place the contribution rates, with the surplus and deficit below each respectively. 
Multiply the contribution rates by their respective surpluses or deficits, and add these to form the dividend. 
Add the surplus and deficit to form the divisor. 
Divide the dividend by the divisor to find the result. If there is a remainder, simplify it. 
For cases where the surplus and deficit are for the same item being purchased, subtract the smaller contribution rate from the larger one. 
Use the remainder to simplify both the divisor and the dividend. 
The dividend gives the price of the item, and the divisor gives the number of people.

Answer: *a* people, and the price of the chickens is *b*.
"""

# 人出九，盈十一
出率1 = 9
盈 = 11

# 人出六，不足十六
出率2 = 6
不足 = 16

# 令維乘所出率，并以為實
實 = (出率1 * 盈) + (出率2 * 不足)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
雞價 = Fraction(實, 法)

# 盈不足相與同其買物者，置所出率，以少減多，餘
餘 = 出率1 - 出率2

# 以約法、實
法 = 法 // 餘
實 = 實 // 餘

# 實為物價，法為人數
b = 雞價
a = 法
"""
Variable 'b' has wrong value. Expected: 70, Actual: 65/9"""
