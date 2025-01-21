"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：醇酒 a升 ，行酒 b斗 。
"""

"""
Suppose there is pure wine (醇酒) worth 50 qian per dou, and diluted wine (行酒) worth 10 qian per dou.
Now, with 30 qian, one can obtain 2 dou of wine in total.
Question: how much pure wine and diluted wine are obtained respectively?

The procedure says: Suppose there are 5 sheng of pure wine and 1 dou 5 sheng of diluted wine, with an excess of 10 qian.
Suppose there are 2 sheng of pure wine and 1 dou 8 sheng of diluted wine, with a deficit of 2 qian.
The procedure for excess and deficit (盈不足術) says: Place the rates of the items being sold, with the excess and deficit below each.
Multiply the rates by the excess and deficit, respectively, and sum them to form the dividend.
Sum the excess and deficit to form the divisor.
Divide the dividend by the divisor to find the unit amount. If there is a remainder, adjust it.
For the excess and deficit corresponding to the same item being purchased, place the rates of the items being sold, subtract the smaller from the larger, and reduce the divisor and dividend proportionally.
The dividend becomes the price of the item, and the divisor becomes the total quantity.

Answer: *a* sheng of pure wine, and *b* dou of diluted wine.
"""

# 醇酒一斗，直錢五十
醇酒價 = 50

# 行酒一斗，直錢一十
行酒價 = 10

# 錢三十，得酒二斗
總錢 = 30
總酒 = 2  # in dou

# 假令醇酒五升，行酒一斗五升，有餘一十
假醇酒1 = 5 / 10  # 5 sheng = 0.5 dou
假行酒1 = 1.5  # 1 dou 5 sheng = 1.5 dou
盈1 = 10

# 令之醇酒二升，行酒一斗八升，不足二
假醇酒2 = 2 / 10  # 2 sheng = 0.2 dou
假行酒2 = 1.8  # 1 dou 8 sheng = 1.8 dou
不足2 = -2

# 盈不足術
# 置所出率，盈、不足各居其下
率1 = 醇酒價 * 假醇酒1 + 行酒價 * 假行酒1
率2 = 醇酒價 * 假醇酒2 + 行酒價 * 假行酒2

# 令維乘所出率，并以為實
實 = 盈1 * 率2 + abs(不足2) * 率1

# 并盈、不足為法
法 = 盈1 + abs(不足2)

# 實如法而一
單位量 = Fraction(實, 法)

# 醇酒 a升
a = 單位量 * 假醇酒1 * 10  # Convert to sheng

# 行酒 b斗
b = 單位量 * 假行酒1

a, b
"""
Code error: both arguments should be Rational instances"""
