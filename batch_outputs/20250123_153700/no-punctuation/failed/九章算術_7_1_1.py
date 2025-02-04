"""
今有共買雞人出九盈十一人出六不足十六問人數雞價各幾何
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰 a人 雞價 b 
"""

"""
Suppose there is a group of people buying chickens. One person contributes 9, which exceeds the required amount by 11. Another person contributes 6, which falls short by 16.
Question: What is the number of people and the price of the chickens?

The procedure for surplus and deficit says: Place the contribution rates, with the surplus and deficit below each. Multiply the contribution rates by their respective surplus or deficit, and sum them to form the dividend. Sum the surplus and deficit to form the divisor. Divide the dividend by the divisor to find the price of the item. If there is a remainder, adjust it. The surplus and deficit must match the item being purchased. Place the contribution rates, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend. The result of the division gives the price of the item, and the divisor gives the number of people.

Answer: *a* people, chicken price *b*.
"""

# 人出九盈十一
出率1 = 9
盈1 = 11

# 人出六不足十六
出率2 = 6
不足2 = 16

# 置所出率，盈不足各居其下，令維乘所出率并以為實
實 = (出率1 * 盈1) + (出率2 * 不足2)

# 并盈不足為法
法 = 盈1 + 不足2

# 實如法而一，有分者通之
雞價 = Fraction(實, 法)

# 盈不足相與同其買物者，置所出率，以少減多，餘以約法實
餘 = 出率1 - 出率2
法 = Fraction(法, 餘)
實 = Fraction(實, 餘)

# 實為物價，法為人數
b = 雞價
a = 法
"""
Variable 'b' has wrong value. Expected: 70, Actual: 65/9"""
