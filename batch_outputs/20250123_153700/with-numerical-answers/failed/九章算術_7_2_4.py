"""
今有共買璡，人出半，盈四；人出少半，不足三。問︰人數、璡價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a(=42)人 ，璡價 b(=17) 。
"""

"""
Suppose there is a group of people jointly buying a jade item. 
If each person contributes half a unit, there is an excess of 4 units.
If each person contributes less than half a unit, there is a shortfall of 3 units.
Question: how many people are there, and what is the price of the jade?

The procedure for surplus and deficit says: Place the contribution rates, with the surplus and deficit below them respectively.
Multiply the contribution rates by their respective surpluses or deficits, and add them together to form the dividend.
Add the surplus and deficit together to form the divisor.
Divide the dividend by the divisor to find one unit. If there is a fraction, simplify it.
For cases where the surplus and deficit relate to the same purchased item, subtract the smaller contribution rate from the larger one.
The remainder is used to simplify the divisor and dividend.
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a*(=42) people, and the price of the jade is *b*(=17).
"""

# 人出半，盈四
所出率多 = Fraction(1, 2)
盈 = 4

# 人出少半，不足三
所出率少 = Fraction(1, 2) - Fraction(1, 2)
不足 = 3

# 令維乘所出率，并以為實
實 = (所出率多 * 盈) + (所出率少 * 不足)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
單位 = Fraction(實, 法)

# 盈不足相與同其買物者，置所出率，以少減多，餘
餘 = 所出率多 - 所出率少

# 以約法、實
約法 = 法 / 餘
約實 = 實 / 餘

# 實為物價，法為人數
b = 約實  # 17 (璡價)
a = 約法  # 42 (人數)
"""
Variable 'a' has wrong value. Expected: 42, Actual: 14
Variable 'b' has wrong value. Expected: 17, Actual: 4"""
