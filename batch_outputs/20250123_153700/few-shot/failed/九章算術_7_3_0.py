"""
今有共買牛，七家共出一百九十，不足三百三十；九家共出二百七十，盈三十。問︰家數、牛價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a家 ，牛價 b 。
"""

"""
Suppose there is a group buying a cow. 
Seven households together contribute 190, which is 330 short.
Nine households together contribute 270, which is 30 in excess.
Question: how many households are there, and what is the price of the cow?

The procedure for surplus and deficit says:
Place the contribution rates, with the surplus and deficit below them respectively.
Multiply the contribution rates crosswise, and add them to form the dividend.
Add the surplus and deficit to form the divisor.
Divide the dividend by the divisor to obtain 1 unit.
If there is a remainder, simplify it.
For those sharing the same purchased item, place the contribution rates, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a* households, and the price of the cow is *b*.
"""

from fractions import Fraction

# 七家共出一百九十，不足三百三十
家數1 = 7
出率1 = 190
不足 = 330

# 九家共出二百七十，盈三十
家數2 = 9
出率2 = 270
盈 = 30

# 置所出率，盈、不足各居其下
# 令維乘所出率，并以為實
實 = (家數1 * 出率2) + (家數2 * 出率1)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
一 = Fraction(實, 法)

# 盈不足相與同其買物者，置所出率，以少減多
餘 = 出率2 - 出率1

# 以約法、實
法 = abs(餘)
實 = 一 * 法

# 實為物價，法為人數
b = 實  # 牛價
a = 法  # 家數
"""
Variable 'a' has wrong value. Expected: 126, Actual: 80
Variable 'b' has wrong value. Expected: 3750, Actual: 800"""
