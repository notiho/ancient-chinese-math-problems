"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：醇酒 a升 ，行酒 b斗 。
"""

"""
Suppose there is pure wine (醇酒) costing 50 qian per dou, and diluted wine (行酒) costing 10 qian per dou.
Now, with 30 qian, 2 dou of wine are obtained.
Question: how much pure wine and diluted wine are obtained respectively?

The procedure says: Suppose 5 sheng of pure wine and 1 dou 5 sheng of diluted wine are obtained, leaving an excess of 10 qian.
Suppose 2 sheng of pure wine and 1 dou 8 sheng of diluted wine are obtained, falling short by 2 qian.

The procedure for surplus and deficit (盈不足術) says: Place the price rates of the items, with the surplus and deficit below each.
Multiply the price rates by their respective surplus or deficit, and sum them to obtain the dividend.
Sum the surplus and deficit to obtain the divisor.
Divide the dividend by the divisor to obtain the result.
If there is a fraction, simplify it.
For the surplus and deficit, adjust the quantities of the items accordingly.

Answer: *a* sheng of pure wine, and *b* dou of diluted wine.
"""

from fractions import Fraction

# 醇酒一斗，直錢五十
醇酒率 = 50

# 行酒一斗，直錢一十
行酒率 = 10

# 錢三十，得酒二斗
總錢 = 30
總酒 = 2  # in dou

# 假令醇酒五升，行酒一斗五升，有餘一十
盈_醇酒 = 5 / 10  # 5 sheng = 0.5 dou
盈_行酒 = 1.5  # 1 dou 5 sheng = 1.5 dou
盈 = 10  # surplus of 10 qian

# 令之醇酒二升，行酒一斗八升，不足二
不足_醇酒 = 2 / 10  # 2 sheng = 0.2 dou
不足_行酒 = 1.8  # 1 dou 8 sheng = 1.8 dou
不足 = -2  # deficit of 2 qian

# 盈不足術
# 置所出率，盈、不足各居其下
盈實 = 醇酒率 * 盈_醇酒 + 行酒率 * 盈_行酒
不足實 = 醇酒率 * 不足_醇酒 + 行酒率 * 不足_行酒

# 令維乘所出率，并以為實
實 = 盈 * 不足實 - 不足 * 盈實

# 并盈、不足為法
法 = 盈 - 不足

# 實如法而一
醇酒量 = Fraction(實, 法)

# 醇酒量為 a 升
a = 醇酒量 * 10  # Convert dou to sheng

# 行酒量為 b 斗
行酒量 = 總酒 - 醇酒量
b = 行酒量
"""
Code error: both arguments should be Rational instances"""
