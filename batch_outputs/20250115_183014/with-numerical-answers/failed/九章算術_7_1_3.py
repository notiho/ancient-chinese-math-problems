"""
今有共買雞，人出九，盈十一；人出六，不足十六。問︰人數、雞價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a(=9)人 ，雞價 b(=70) 。
"""

"""
Suppose a group of people jointly buys chickens. If each person contributes 9, there is a surplus of 11. If each person contributes 6, there is a deficit of 16.
Question: how many people are there, and what is the price of the chickens?

The procedure for surplus and deficit says: Place the contribution rates, with the surplus and deficit below each.
Multiply the contribution rates by their respective surplus or deficit, and add these to form the dividend.
Add the surplus and deficit to form the divisor.
Divide the dividend by the divisor to find the unit. If there is a fraction, simplify it.
For the surplus and deficit to jointly correspond to the same purchased item, place the contribution rates, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend.
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a*(=9) people, and the price of the chickens is *b*(=70).
"""

# 置所出率
出率_盈 = 9
出率_不足 = 6

# 盈、不足各居其下
盈 = 11
不足 = 16

# 令維乘所出率，并以為實
實 = (出率_盈 * 盈) + (出率_不足 * 不足)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
單位 = Fraction(實, 法)

# 盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實
餘 = 出率_盈 - 出率_不足
法 = Fraction(法, 餘)
實 = Fraction(實, 餘)

# 實為物價，法為人數
b = 實  # 雞價 = 70
a = 法  # 人數 = 9
"""
Variable 'b' has wrong value. Expected: 70, Actual: 65"""
