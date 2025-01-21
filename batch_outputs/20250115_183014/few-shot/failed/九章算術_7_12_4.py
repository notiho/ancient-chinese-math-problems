"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：醇酒 a升 ，行酒 b斗 。
"""

"""
Suppose there is pure wine (醇酒) priced at 50 qian per dou, and diluted wine (行酒) priced at 10 qian per dou.
Now, with 30 qian, 2 dou of wine is obtained in total.
Question: how much pure wine and diluted wine are obtained respectively?

The procedure says: Suppose 5 sheng of pure wine and 1 dou 5 sheng of diluted wine are taken, leaving an excess of 10 qian.
Suppose 2 sheng of pure wine and 1 dou 8 sheng of diluted wine are taken, falling short by 2 qian.
The procedure for surplus and deficit (盈不足術) says: Place the rates of the items being purchased, with the surplus and deficit below each.
Cross-multiply the rates of the items being purchased, and sum them to form the dividend.
Sum the surplus and deficit to form the divisor.
Divide the dividend by the divisor to find the unit amount. If there is a remainder, adjust it proportionally.
For the surplus and deficit, adjust the amounts of the items being purchased proportionally by the rates.

Answer: Pure wine is *a* sheng, and diluted wine is *b* dou.
"""

from fractions import Fraction

# 醇酒一斗，直錢五十
醇酒價 = 50

# 行酒一斗，直錢一十
行酒價 = 10

# 錢三十，得酒二斗
總錢 = 30
總酒 = 2  # in dou

# 假令醇酒五升，行酒一斗五升，有餘一十
盈_醇酒 = 5  # in sheng
盈_行酒 = 1 + Fraction(5, 10)  # 1 dou 5 sheng = 1.5 dou
盈 = 10  # surplus in qian

# 令之醇酒二升，行酒一斗八升，不足二
不足_醇酒 = 2  # in sheng
不足_行酒 = 1 + Fraction(8, 10)  # 1 dou 8 sheng = 1.8 dou
不足 = -2  # deficit in qian

# 盈不足術
# 置所出率，盈、不足各居其下
盈率 = 醇酒價 * 盈_醇酒 + 行酒價 * 盈_行酒
不足率 = 醇酒價 * 不足_醇酒 + 行酒價 * 不足_行酒

# 令維乘所出率，并以為實
實 = abs(不足) * 盈率 + abs(盈) * 不足率

# 并盈、不足為法
法 = abs(盈) + abs(不足)

# 實如法而一
單位量 = Fraction(實, 法)

# 醇酒量 (a) = 盈量 * 單位量
a = 盈_醇酒 * 單位量

# 行酒量 (b) = 總酒 - 醇酒量
b = 總酒 - a / 10  # Convert a from sheng to dou

# 醇酒 a升，行酒 b斗
a = a  # in sheng
b = b  # in dou
"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 1425/2
Variable 'b' has wrong value. Expected: 7/4, Actual: -277/4"""
