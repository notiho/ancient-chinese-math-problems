"""
今有共買牛，七家共出一百九十，不足三百三十；九家共出二百七十，盈三十。問︰家數、牛價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a家 ，牛價 b 。
"""

#----- content starts here -----
"""
Suppose there is a group buying a cow. 
Seven families together contribute 190, which is 330 short. 
Nine families together contribute 270, which is 30 extra. 
Question: how many families are there, and what is the price of the cow?

The procedure for surplus and deficit says: 
Place the contribution rates, with the surplus and deficit below them. 
Multiply the contribution rates by their respective values, and sum them to form the dividend. 
Sum the surplus and deficit to form the divisor. 
Divide the dividend by the divisor to find the result. 
If there is a remainder, simplify it. 
For the surplus and deficit cases involving the same item being purchased, 
place the contribution rates, subtract the smaller from the larger, and simplify the divisor and dividend. 
The dividend gives the price of the item, and the divisor gives the number of families.

Answer: *a* families, and the price of the cow is *b*.
"""

from fractions import Fraction

# Given data
七家 = 7
七家出 = 190
七家不足 = 330

九家 = 9
九家出 = 270
九家盈 = 30

# 盈不足術
# 置所出率，盈、不足各居其下
所出率_七家 = 七家
所出率_九家 = 九家

盈 = 九家盈
不足 = 七家不足

# 令維乘所出率，并以為實
實 = (所出率_七家 * 盈) + (所出率_九家 * 不足)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
家數 = Fraction(實, 法)

# 盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實
所出率差 = abs(所出率_九家 - 所出率_七家)
法 = Fraction(法, 所出率差)
實 = Fraction(實, 所出率差)

# 實為物價，法為人數
牛價 = 實
a = 家數
b = 牛價

# Final results
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 126, Actual: 53/6
Variable 'b' has wrong value. Expected: 3750, Actual: 1590"""
