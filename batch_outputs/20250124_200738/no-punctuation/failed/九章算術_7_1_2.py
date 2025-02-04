"""
今有共買雞人出九盈十一人出六不足十六問人數雞價各幾何
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰 a人 雞價 b 
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys chickens. One person contributes 9 coins, which is 11 coins more than needed. Another person contributes 6 coins, which is 16 coins less than needed.
Question: how many people are there, and what is the price of the chicken?

The procedure for the "excess and deficit" method says:
Place the contributions (rates of contribution) under the respective excess and deficit amounts.
Multiply the contributions by their respective excess or deficit amounts, and sum them to obtain the dividend.
Sum the excess and deficit amounts to obtain the divisor.
Divide the dividend by the divisor to obtain the price of the item (chicken). If there is a remainder, adjust it proportionally.
The excess and deficit amounts must correspond to the same item being purchased.
To find the number of people, place the contributions. Subtract the smaller contribution from the larger one, and use the remainder to simplify the divisor and dividend.
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: there are *a* people, and the price of the chicken is *b*.
"""

# 人出九盈十一
出率1 = 9
盈 = 11

# 人出六不足十六
出率2 = 6
不足 = 16

# 置所出率，盈不足各居其下，令維乘所出率并以為實
實 = (出率1 * 不足) + (出率2 * 盈)

# 并盈不足為法
法 = 盈 + 不足

# 實如法而一，得雞價
雞價 = Fraction(實, 法)

# 置所出率，以少減多，餘以約法實
餘 = 出率1 - 出率2
法 = Fraction(法, 餘)
實 = Fraction(實, 餘)

# 實為物價，法為人數
a = 法  # 人數
b = 雞價  # 雞價#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 70, Actual: 70/9"""
