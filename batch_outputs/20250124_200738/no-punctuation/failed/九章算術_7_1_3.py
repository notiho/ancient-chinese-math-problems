"""
今有共買雞人出九盈十一人出六不足十六問人數雞價各幾何
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰 a人 雞價 b 
"""

#----- content starts here -----
"""
Suppose there is a group of people buying chickens. One person contributes 9, which is 11 more than needed. Another person contributes 6, which is 16 less than needed.
Question: how many people are there, and what is the price of the chicken?

The procedure for the "excess and deficit" method says:
Place the contribution rates, with the excess and deficit values below them.
Multiply the contribution rates by their respective excess or deficit values, and sum these to obtain the dividend.
Sum the excess and deficit values to obtain the divisor.
Divide the dividend by the divisor to obtain the price of the item. If there is a remainder, simplify it.
The excess and deficit values are treated equally.
For the number of people, subtract the smaller contribution rate from the larger one, and use the remainder to simplify the divisor and dividend.
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a* people, and the price of the chicken is *b*.
"""

# 人出九盈十一
出率1 = 9
盈1 = 11

# 人出六不足十六
出率2 = 6
不足2 = 16

# 置所出率，盈不足各居其下
# 令維乘所出率，并以為實
實 = (出率1 * 盈1) + (出率2 * 不足2)

# 并盈不足為法
法 = 盈1 + 不足2

# 實如法而一
雞價 = Fraction(實, 法)

# 置所出率，以少減多
餘 = 出率1 - 出率2

# 餘以約法實
法 = Fraction(法, 餘)
實 = Fraction(實, 餘)

# 實為物價，法為人數
b = 雞價
a = 法#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 70, Actual: 65/9"""
