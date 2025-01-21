"""
今有共買雞，人出九，盈十一；人出六，不足十六。問︰人數、雞價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，雞價 b 。
"""

"""
Suppose a group of people jointly buys chickens. 
If each person contributes 9, there is an excess of 11.
If each person contributes 6, there is a shortfall of 16.
Question: how many people are there, and what is the price of the chickens?

The procedure for surplus and deficit says:
Place the contribution rates, with the surplus and deficit below each.
Multiply the contribution rates crosswise, and add them to form the dividend.
Add the surplus and deficit to form the divisor.
Divide the dividend by the divisor to get 1 unit. If there is a remainder, simplify it.
If the surplus and deficit correspond to the same item being purchased, 
place the contribution rates, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend.
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a* people, and the price of the chickens is *b*.
"""

from fractions import Fraction

# 人出九，盈十一
出率_1 = 9
盈 = 11

# 人出六，不足十六
出率_2 = 6
不足 = 16

# 置所出率，以少減多，餘
差 = 出率_1 - 出率_2

# 盈、不足相加
盈不足和 = 盈 + 不足

# 令維乘所出率，并以為實
實 = 出率_1 * 不足 + 出率_2 * 盈

# 盈不足為法
法 = 盈不足和

# 實如法而一
雞價 = Fraction(實, 法)

# 法為人數
人數 = Fraction(法, 差)

a = 人數
b = 雞價
"""
Variable 'b' has wrong value. Expected: 70, Actual: 70/9"""
