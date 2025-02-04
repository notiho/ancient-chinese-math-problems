"""
今有共買璡，人出半，盈四；人出少半，不足三。問︰人數、璡價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，璡價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys a jade (璡). 
If each person contributes half, there is an excess of 4. 
If each person contributes less than half, there is a shortfall of 3. 
Question: how many people are there, and what is the price of the jade?

The procedure for surplus and deficit says: Place the contribution rates, with the surplus and deficit below them. 
Multiply the contribution rates by their respective surplus or deficit, and sum these to form the dividend. 
Sum the surplus and deficit to form the divisor. 
Divide the dividend by the divisor to find the result. 
If there is a fraction, simplify it. 
For cases where the surplus and deficit relate to the same item being purchased, subtract the smaller contribution rate from the larger one. 
Use this difference to simplify the divisor and dividend. 
The dividend gives the price of the item, and the divisor gives the number of people.

Answer: *a* people, jade price *b*.
"""

from fractions import Fraction

# 盈、不足各居其下
所出率_盈 = Fraction(1, 2)  # 人出半
盈 = 4  # 盈四

所出率_不足 = Fraction(1, 2) - Fraction(1, 2)  # 人出少半
不足 = 3  # 不足三

# 令維乘所出率，并以為實
實 = (所出率_盈 * 盈) + (所出率_不足 * 不足)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
人數 = Fraction(實, 法)

# 盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實
所出率差 = 所出率_盈 - 所出率_不足
法 = 法 / 所出率差
實 = 實 / 所出率差

# 實為物價，法為人數
a = 人數
b = 實#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 42, Actual: 2/7
Variable 'b' has wrong value. Expected: 17, Actual: 4"""
