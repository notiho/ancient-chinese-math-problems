"""
今有共買牛，七家共出一百九十，不足三百三十；九家共出二百七十，盈三十。問︰家數、牛價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a(=126)家 ，牛價 b(=3750) 。
"""

"""
Suppose there is a group buying cattle. Seven families contribute a total of 190, which is short by 330.
Nine families contribute a total of 270, which exceeds by 30.
Question: how many families are there, and what is the price of the cattle?

The procedure for surplus and deficit says: Place the contribution rates, with the surplus and deficit below them.
Multiply the contribution rates by their respective surplus or deficit, and sum these to obtain the dividend.
Sum the surplus and deficit to obtain the divisor.
Divide the dividend by the divisor to obtain 1 unit. If there is a fraction, simplify it.
For those sharing the same purchase, place the contribution rates, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend is the price of the item, and the divisor is the number of families.

Answer: *a*(=126) families, and the price of the cattle is *b*(=3750).
"""

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
實 = (家數1 * 盈) + (家數2 * 不足)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
單位 = Fraction(實, 法)

# 盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實
餘 = abs(出率2 - 出率1)
法2 = abs(家數2 - 家數1)

# 實為物價，法為人數
b = Fraction(餘 * 單位, 法2)  # 牛價 = 3750
a = Fraction(法2 * b, 餘)  # 家數 = 126
"""
Variable 'a' has wrong value. Expected: 126, Actual: 53/6
Variable 'b' has wrong value. Expected: 3750, Actual: 1060/3"""
