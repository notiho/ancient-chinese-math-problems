"""
今有共買雞人出九盈十一人出六不足十六問人數雞價各幾何
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰 a人 雞價 b 
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys chickens. One person contributes 9 coins and has 11 coins left over. Another person contributes 6 coins but is short by 16 coins.
Question: how many people are there, and what is the price of the chickens?

The procedure for the "excess and deficit" method says:
1. Place the contribution rates (amounts contributed) with the excess and deficit values below them.
2. Multiply the contribution rates by their respective excess or deficit values, and sum these to form the dividend (實).
3. Sum the excess and deficit values to form the divisor (法).
4. Divide the dividend by the divisor to find the price of the item (雞價).
5. If there is a remainder, adjust it proportionally.
6. To find the number of people, subtract the smaller contribution rate from the larger one, and use this difference to simplify the divisor and dividend.
7. The simplified dividend gives the price of the item, and the simplified divisor gives the number of people.

Answer: *a* people, chicken price *b*.
"""

# 人出九盈十一
出率1 = 9
盈1 = 11

# 人出六不足十六
出率2 = 6
不足2 = 16

# 置所出率，盈不足各居其下
# 維乘所出率，并以為實
實 = (出率1 * 盈1) + (出率2 * 不足2)

# 并盈不足為法
法 = 盈1 + 不足2

# 實如法而一
雞價 = Fraction(實, 法)

# 置所出率，以少減多
差 = 出率1 - 出率2

# 餘以約法實
約法 = 法 / 差
約實 = 實 / 差

# 實為物價，法為人數
b = 約實
a = 約法#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 70, Actual: 65.0"""
