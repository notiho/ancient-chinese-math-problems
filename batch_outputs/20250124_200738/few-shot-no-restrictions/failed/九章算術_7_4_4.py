"""
今有共買金，人出四百，盈三千四百；人出三百，盈一百。問︰人數、金價各幾何？
兩盈、兩不足術曰：置所出率，盈、不足各居其下。令維乘所出率，以少減多，餘為實。兩盈、兩不足以少減多，餘為法。實如法而一。有分者通之。
荅曰： a人 。金價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys gold. 
If each person contributes 400, there is a surplus of 3400.
If each person contributes 300, there is a surplus of 100.
Question: how many people are there, and what is the price of the gold?

The procedure says: Place the contribution rates, with the surplus or deficit below each. 
Multiply the contribution rates by the corresponding surplus or deficit, then subtract the smaller product from the larger product to get the dividend.
Subtract the smaller surplus or deficit from the larger surplus or deficit to get the divisor.
Divide the dividend by the divisor to find the number of people.
If there is a remainder, adjust accordingly.

Answer: there are *a* people, and the price of the gold is *b*.
"""

from fractions import Fraction

# Inputs
rate1 = 400  # 每人出400
surplus1 = 3400  # 盈餘3400

rate2 = 300  # 每人出300
surplus2 = 100  # 盈餘100

# Procedure
# 令維乘所出率，以少減多，餘為實
實 = (rate1 * surplus1) - (rate2 * surplus2)

# 兩盈、兩不足以少減多，餘為法
法 = surplus1 - surplus2

# 實如法而一
人數 = Fraction(實, 法)

# 金價 = 每人出資 * 人數 - 盈餘
金價 = rate1 * 人數 - surplus1

# Results
a = 人數
b = 金價

a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 33, Actual: 13300/33
Variable 'b' has wrong value. Expected: 9800, Actual: 5207800/33"""
