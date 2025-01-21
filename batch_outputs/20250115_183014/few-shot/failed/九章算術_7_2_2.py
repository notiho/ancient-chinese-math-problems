"""
今有共買璡，人出半，盈四；人出少半，不足三。問︰人數、璡價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，璡價 b 。
"""

"""
Suppose a group of people jointly buys a jade item. If each person contributes half, there is an excess of 4. 
If each person contributes less than half, there is a shortfall of 3.
Question: how many people are there, and what is the price of the jade item?

The procedure for surplus and shortfall says: Place the contribution rate, with the surplus and shortfall below it respectively.
Multiply the contribution rate by the surplus and shortfall, and add them to form the dividend.
Add the surplus and shortfall to form the divisor.
Divide the dividend by the divisor to get 1. If there is a fraction, simplify it.
For cases where the surplus and shortfall correspond to the same item being purchased, place the contribution rate, subtract the smaller rate from the larger rate, and use the remainder to simplify the divisor and dividend.
The dividend is the price of the item, and the divisor is the number of people.

Answer: *a* people, jade price *b*.
"""

# 人出半
所出率_多 = Fraction(1, 2)

# 盈四
盈 = 4

# 人出少半
所出率_少 = Fraction(1, 2) - Fraction(1, 2)

# 不足三
不足 = 3

# 盈不足各居其下
盈不足 = 盈 +不足
"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
