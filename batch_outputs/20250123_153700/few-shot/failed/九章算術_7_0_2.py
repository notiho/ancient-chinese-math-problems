"""
今有共買物，人出八，盈三；人出七，不足四。問︰人數、物價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，物價 b 。
"""

"""
Suppose a group of people jointly buys an item. If each person contributes 8, there is an excess of 3. If each person contributes 7, there is a shortfall of 4.
Question: how many people are there, and what is the price of the item?

The procedure for the surplus and deficit says:
Place the contribution rates, with the surplus and deficit below them respectively.
Multiply each contribution rate by its corresponding surplus or deficit, then add these to form the dividend.
Add the surplus and deficit to form the divisor.
Divide the dividend by the divisor to find the number of people.
If there is a remainder, simplify it.
For the surplus and deficit jointly buying the item, place the contribution rates.
Subtract the smaller rate from the larger rate, and use the remainder to simplify the divisor and dividend.
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a* people, item price *b*.
"""

# 人出八，盈三
出率1 = 8
盈 = 3

# 人出七，不足四
出率2 = 7
不足 = 4

# 令維乘所出率，并以為實
實 = (出率1 * 盈) + (出率2 * 不足)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一。有分者，通之。
人數 = Fraction(實, 法)

# 置所出率，以少減多，餘
餘 = 出率1 - 出率2

# 以約法、實
法 = Fraction(法, 餘)
實 = Fraction(實, 餘)

# 實為物價，法為人數
a = 法
b = 實
"""
Variable 'b' has wrong value. Expected: 53, Actual: 52"""
