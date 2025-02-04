"""
今有共買物，人出八，盈三；人出七，不足四。問︰人數、物價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a(=7)人 ，物價 b(=53) 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys an item. If each person contributes 8, there is an excess of 3. If each person contributes 7, there is a shortfall of 4.
Question: how many people are there, and what is the price of the item?

The procedure for "excess and shortfall" says:
Place the contribution rates, with the excess and shortfall below them respectively.
Multiply the contribution rates by their respective excess or shortfall, and add these to form the dividend.
Add the excess and shortfall to form the divisor.
Divide the dividend by the divisor to find the number of people. If there is a remainder, simplify it.
For the price of the item, take the difference between the contribution rates, and reduce the divisor and dividend accordingly.
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a*(=7) people, and the price of the item is *b*(=53).
"""

# 人出八，盈三
出率1 = 8
盈 = 3

# 人出七，不足四
出率2 = 7
不足 = 4

# 令維乘所出率，并以為實
實 = (出率1 * 不足) + (出率2 * 盈)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
人數 = Fraction(實, 法)

# 以少減多，餘，以約法、實
差 = 出率1 - 出率2
物價 = Fraction(差 * 實, 法)

# Final results
a = 人數  # 7
b = 物價  # 53#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 7, Actual: 53/7
Variable 'b' has wrong value. Expected: 53, Actual: 53/7"""
