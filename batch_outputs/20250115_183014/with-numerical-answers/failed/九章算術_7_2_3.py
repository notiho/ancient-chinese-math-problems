"""
今有共買璡，人出半，盈四；人出少半，不足三。問︰人數、璡價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a(=42)人 ，璡價 b(=17) 。
"""

"""
Suppose people jointly buy a jade (璡). 
If each person contributes half, there is an excess of 4.
If each person contributes less than half, there is a shortfall of 3.
Question: how many people are there, and what is the price of the jade?

The procedure for "excess and shortfall" says:
Place the contribution rates, with the excess and shortfall below each respectively.
Multiply the contribution rates by their respective excess or shortfall, and add them together to form the dividend.
Add the excess and shortfall together to form the divisor.
Divide the dividend by the divisor to find the base unit. 
If there is a fraction, simplify it.
For cases where the excess and shortfall are related to the same purchased item, place the contribution rates, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend.
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a*(=42) people, and the price of the jade is *b*(=17).
"""

# 人出半，盈四
所出率_盈 = Fraction(1, 2)
盈 = 4

# 人出少半，不足三
所出率_不足 = Fraction(1, 2) - Fraction(1, 2)
不足 = 3

# 令維乘所出率，并以為實
實 = (所出率_盈 * 盈) + (所出率_不足 * 不足)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
單位 = Fraction(實, 法)

# 盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實
餘 = 所出率_盈 - 所出率_不足
法 = 法 / 餘
實 = 實 / 餘

# 實為物價，法為人數
b = 實  # 璡價 = 17
a = 法  # 人數 = 42
"""
Variable 'a' has wrong value. Expected: 42, Actual: 14
Variable 'b' has wrong value. Expected: 17, Actual: 4"""
