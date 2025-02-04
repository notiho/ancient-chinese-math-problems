"""
今有共買雞，人出九，盈十一；人出六，不足十六。問︰人數、雞價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，雞價 b 。
"""

"""
Suppose a group of people collectively buys chickens. 
If each person contributes 9, there is an excess of 11. 
If each person contributes 6, there is a shortfall of 16. 
Question: how many people are there, and what is the price of the chickens?

The procedure for surplus and deficit says: Place the contribution rates, with the surplus and deficit below each. 
Multiply the contribution rates by their respective surplus or deficit, and add them to form the dividend. 
Add the surplus and deficit to form the divisor. 
Divide the dividend by the divisor to find one unit. If there is a remainder, simplify it. 
If the surplus and deficit are for the same item being purchased, subtract the smaller contribution rate from the larger one. 
Use the remainder to simplify the divisor and dividend. 
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a* people, chicken price *b*.
"""

# 置所出率
出率_盈 = 9  # 每人出9，盈11
出率_不足 = 6  # 每人出6，不足16

# 盈、不足各居其下
盈 = 11
不足 = 16

# 令維乘所出率，并以為實
實 = (出率_盈 * 盈) + (出率_不足 * 不足)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
單位 = Fraction(實, 法)

# 盈不足相與同其買物者，置所出率，以少減多，餘
餘 = 出率_盈 - 出率_不足

# 以約法、實
法 = 法 // 餘
實 = 實 // 餘

# 實為物價，法為人數
b = 實  # 雞價
a = 法  # 人數
"""
Variable 'b' has wrong value. Expected: 70, Actual: 65"""
