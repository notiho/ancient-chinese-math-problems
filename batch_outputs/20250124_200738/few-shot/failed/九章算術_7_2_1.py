"""
今有共買璡，人出半，盈四；人出少半，不足三。問︰人數、璡價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，璡價 b 。
"""

#----- content starts here -----
"""
Suppose there is a group buying a jade item. If each person contributes half, there is an excess of 4. 
If each person contributes less than half, there is a shortfall of 3. 
Question: how many people are there, and what is the price of the jade item?

The procedure for surplus and deficit says: Place the contribution rates, with the surplus and deficit below each. 
Multiply the contribution rates by their respective surplus or deficit, and sum them to form the dividend. 
Sum the surplus and deficit to form the divisor. 
Divide the dividend by the divisor to find 1. If there is a fraction, simplify it. 
For cases where the surplus and deficit are related to the same item being purchased, subtract the smaller contribution rate from the larger one. 
Use the remainder to simplify the divisor and dividend. 
The dividend gives the price of the item, and the divisor gives the number of people.

Answer: *a* people, and the price of the jade item is *b*.
"""

from fractions import Fraction

# 所出率
所出率多 = Fraction(1, 2)  # 人出半
所出率少 = Fraction(1, 4)  # 人出少半

# 盈、不足
盈 = 4
不足 = 3

# 令維乘所出率，并以為實
實 = (所出率多 * 不足) + (所出率少 * 盈)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
一 = Fraction(實, 法)

# 盈不足相與同其買物者，置所出率，以少減多，餘
餘 = 所出率多 - 所出率少

# 以約法、實
法 = 法 * 餘
實 = 實 * 餘

# 實為物價，法為人數
b = 實  # 璡價
a = 法  # 人數#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 42, Actual: 7/4
Variable 'b' has wrong value. Expected: 17, Actual: 5/8"""
