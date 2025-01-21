"""
今有共買雞人出九盈十一人出六不足十六問人數雞價各幾何
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰 a人 雞價 b 
"""

"""
Suppose a group of people jointly buys chickens. One person contributes 9 and has 11 extra, while another contributes 6 and is short by 16.
Question: how many people are there, and what is the price of one chicken?

The procedure for the "Excess and Deficit" method says:
1. Place the amounts contributed (rates) and the excess/deficit values below them.
2. Multiply the rates by their respective excess/deficit values, and sum these products to form the dividend (實).
3. Sum the excess and deficit values to form the divisor (法).
4. Divide the dividend by the divisor to find the price of the item (雞價).
5. If there is a remainder, adjust it to ensure consistency.
6. To find the number of people, subtract the smaller rate from the larger rate, and use the remainder to simplify the divisor and dividend.
7. The simplified dividend divided by the simplified divisor gives the number of people.

Answer: *a* people, and the price of one chicken is *b*.
"""

# 人出九盈十一
率1 = 9
盈1 = 11

# 人出六不足十六
率2 = 6
不足2 = 16

# 置所出率，盈不足各居其下
# 維乘所出率并以為實
實 = (率1 * 盈1) + (率2 * 不足2)

# 并盈不足為法
法 = 盈1 + 不足2

# 實如法而一
雞價 = Fraction(實, 法)

# 置所出率，以少減多
餘 = 率1 - 率2

# 餘以約法實
約法 = 法 // 餘
約實 = 實 // 餘

# 實為物價，法為人數
a = 約法  # 人數
b = 約實  # 雞價
"""
Variable 'b' has wrong value. Expected: 70, Actual: 65"""
